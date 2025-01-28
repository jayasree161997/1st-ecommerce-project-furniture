from django.http import HttpResponse
import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout,login as auth_login
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.timezone import now
from django.core.cache import cache
from products.models import Product,ProductVariant


# Create your views here.
def index(request):
    return render(request,'user/index.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return render(request,"user/index.html")

        else:
            return redirect('signup')
    return render(request,'user/login.html')
  
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        otp = random.randint(1000, 9999)
        expiry_time = now() + datetime.timedelta(minutes=5)  # OTP expires in 5 minutes

        # Store OTP and expiry in the session or cache
        cache.set(email, {'otp': otp, 'expiry': expiry_time}, timeout=300)

        send_mail(
            'Your OTP for Verification',
            f'Your OTP is: {otp}. It will expire in 5 minutes.',
            'jayasreeidhunov@gmail.com',  # Replace email
            [email],
            fail_silently=False,
        )

        request.session['email'] = email
        messages.success(request, "OTP sent to your email. Please verify.")
        return redirect('otp_verification')

    return render(request, 'user/signup.html')


def otp_verification(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        email = request.session.get('email')

        otp_data = cache.get(email)
        if not otp_data:
            messages.error(request, "OTP expired. Please request a new one.")
            return redirect('signup')  # Redirect to signup or OTP resend

        stored_otp = otp_data['otp']
        expiry = otp_data['expiry']

        if now() > expiry:
            messages.error(request, "OTP expired. Please request a new one.")
            return redirect('signup')

        if str(entered_otp) == str(stored_otp):
            cache.delete(email)  # Clear OTP from cache
            messages.success(request, "OTP verified successfully!")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'user/otp_verification.html')


def resend_otp(request):
    email = request.session.get('email')
    if not email:
        messages.error(request, "Session expired. Please sign up again.")
        return redirect('signup')

    otp = random.randint(1000, 9999)
    expiry_time = now() + datetime.timedelta(minutes=5)

    cache.set(email, {'otp': otp, 'expiry': expiry_time}, timeout=300)

    send_mail(
        'Your New OTP for Verification',
        f'Your new OTP is: {otp}. It will expire in 5 minutes.',
        'jayasreeidhunov@gmail.com',  
        [email],
        fail_silently=False,
    )

    messages.success(request, "A new OTP has been sent to your email.")
    return redirect('otp_verification')
