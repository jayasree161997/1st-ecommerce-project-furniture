from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Example:
    path('', views.index, name='index'),
    # path("shop/",views.shop_view,name='shop'),
    path("signup/", views.signup, name="signup"),
    path("login/",views.user_login,name='login'),
    path("otp_verification/",views.otp_verification,name='otp_verification'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),
     
] 

