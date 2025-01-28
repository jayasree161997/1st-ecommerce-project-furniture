from django.urls import path
from . import views


app_name = 'custom_admin'

urlpatterns = [
    path('', views.signin, name="signin"),  
    path('index/', views.index, name='index'),  
    path('home/', views.home, name='home'), 
    path('users/', views.user_management, name='users'), 
    path('block_unblock_user/', views.block_unblock_user, name='block_unblock_user'),  
    path('products/', views.products_view, name='products_view'), 
    path('products/add/', views.add_product, name='add_products'),  
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_products'),  
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_products'),  
    path('products/<int:product_id>/', views.products_details, name='products_details'), 
    path('productmanagement/',views.productmanagement,name='productmanagement'),
    path('product_view/',views.product_view,name='product_view'),
    path('categories/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('add_variant/', views.add_variant, name='add_variant'),
    path('variants/', views.variant_list, name='variant_list'),
]



