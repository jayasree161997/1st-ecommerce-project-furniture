from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
    path('products/',views.products,name='products'),
    path('products_details/<int:product_id>/',views.product_details,name='products_details'),
    path('thumbnails/', views.thumbnail_list, name='thumbnail_list'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    
    
]
