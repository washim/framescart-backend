from django.db import models

PRODUCT_TYPE = [
    ('border_frame', 'Border Frame'), 
    ('canvas_frame', 'Canvas Frame'), 
    ('tshirt', 'Tshirt')
]

class Product(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=50, default='canvas_frame')
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    mrp = models.DecimalField(max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField("Create Date", auto_now_add=True)
    modified_at = models.DateTimeField("Modified Date", auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
    
class ProductAttribute(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ProductAttributeItem(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, related_name='product_attribute_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class ProductOption(models.Model):
    product = models.ForeignKey(Product, related_name='product_options', on_delete=models.CASCADE)
    product_attribute = models.ForeignKey(ProductAttribute, related_name='product_options', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['product', 'product_attribute']
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads')
    caption = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.image.name