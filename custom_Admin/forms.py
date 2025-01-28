from django import forms
from products.models import Product,ProductVariant,Category
# ,ProductThumbnail


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'brand', 'price', 'quantity', 'original_price',
            'discount_percentage', 'stock_status', 'sold', 'main_image', 
            'material', 'dimensions', 'weight', 'warranty','category'
        ]
        # ,ProductThumbnail
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'main_image': forms.ClearableFileInput(),
            
        }
        # 'thumbnail_images': forms.CheckboxSelectMultiple(),
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'main_image': 'Main Product Image',
        }
# def __init__(self, *args, **kwargs):
#         super(ProductForm, self).__init__(*args, **kwargs)
#         self.fields['thumbnail_images'].queryset = ProductThumbnail.objects.all()
#         self.fields['thumbnail_images'].required = False    
            
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


# Form for the ProductVariant model
class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product', 'variant_name', 'variant_value', 'color_image']
        widgets = {
            'color_image': forms.ClearableFileInput(),
        }
        labels = {
            'variant_name': 'Variant Name',
            'variant_value': 'Variant Value (e.g., Color or Size)',
            'color_image': 'Image for Variant (if applicable)',
        }


# # Form for the ProductThumbnail model
# class ProductThumbnailForm(forms.ModelForm):
#     class Meta:
#         model = ProductThumbnail
#         fields = ['image', 'alt_text']
#         widgets = {
#             'image': forms.ClearableFileInput(),
#         }
#         labels = {
#             'image': 'Thumbnail Image',
#             'alt_text': 'Alternative Text for Thumbnail',
#         }


