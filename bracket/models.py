from django.db import models

class CategoryItem(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
    
class Category(models.Model):
    product = models.ForeignKey("catalog.Product", related_name='categories', on_delete=models.CASCADE)
    category_item = models.ForeignKey(CategoryItem, related_name='category_items', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['product', 'category_item']
