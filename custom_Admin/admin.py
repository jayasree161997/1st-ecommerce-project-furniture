from django.contrib import admin

from products. models import Product, ProductVariant,Category,ProductThumbnail

# Register your models here.


admin.site.register(Product)
admin.site.register( ProductVariant)
admin.site.register( ProductThumbnail)
admin.site.register(Category)


class ProductThumbnailAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image')  # Display fields in the admin panel
    search_fields = ('alt_text',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class ProductVariantAdmin(admin.ModelAdmin):
    # list_display = ['variant_name', 'variant_value', 'product', 'color_image']
    list_display = ('id', 'product', 'variant_name', 'variant_value')
    list_filter = ('product',)
    search_fields = ('variant_name', 'variant_value')

