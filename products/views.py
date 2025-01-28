from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from products.models import Product,ProductVariant,Category,ProductThumbnail
from django.core.paginator import Paginator






def products(request):
    category_id = request.GET.get('category_id')
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category).order_by('id')
    else:
        products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'user/products.html', {'products': products, 'categories': categories})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id) 
    variants = ProductVariant.objects.filter(product=product)
    context = {
        'product': product,
        'variants': variants
    }
    return render(request, 'user/products_details.html', context)

def product_view(request):
    products = Product.objects.all()
    return render(request, 'custom_admin/product_view.html', {'products': products})

def thumbnail_list(request):
    thumbnails = ProductThumbnail.objects.all()
    return render(request, "thumbnails.html", {"thumbnails": thumbnails})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'custom_Admin/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'user/category_detail.html', {'category': category, 'products': products})
