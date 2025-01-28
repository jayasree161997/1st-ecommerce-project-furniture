from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name", blank=True, null=True)
    description = models.TextField(verbose_name="Category Description", blank=True, null=True)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category",blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name="Product Name")
    description = models.TextField(verbose_name="Product Description")
    brand = models.CharField(max_length=100, verbose_name="Brand", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    quantity = models.IntegerField(null=False , blank=False)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Original Price", blank=True, null=True)
    discount_percentage = models.IntegerField(verbose_name="Discount Percentage", blank=True, null=True)
    stock_status = models.BooleanField(default=True, verbose_name="In Stock")
    sold = models.PositiveIntegerField(verbose_name="Units Sold", default=0)

    main_image = models.ImageField(upload_to="products/main_images/", verbose_name="Main Image",default="products/main_images/default.jpg")
    thumbnail_images = models.ManyToManyField("ProductThumbnail", related_name="product_thumbnails", verbose_name="Thumbnail Images")


    material = models.CharField(max_length=100, verbose_name="Material", blank=True, null=True)
    dimensions = models.CharField(max_length=100, verbose_name="Dimensions", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", blank=True, null=True)
    warranty = models.CharField(max_length=100, verbose_name="Warranty", blank=True, null=True)

    

    def __str__(self):
        return self.name


    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=50, null=False, blank=False) 
    variant_value = models.CharField(max_length=50, null=True, blank=True)  
    color_image = models.ImageField(upload_to="products/color_variants", verbose_name="Color Image")
    

    def __str__(self):
        return f"{self.variant_name}: {self.variant_value or 'N/A'} ({self.product.name})"
    

class ProductThumbnail(models.Model):
    product = models.ForeignKey(Product, related_name='thumbnails', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/thumbnails", verbose_name="Thumbnail Image")
    alt_text = models.CharField(max_length=100, verbose_name="Alt Text", blank=True, null=True)

    def __str__(self):
        return self.alt_text or "Thumbnail"
        
    
