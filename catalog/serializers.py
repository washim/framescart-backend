from rest_framework import serializers
from .models import Product, ProductOption, ProductAttribute, ProductAttributeItem, ProductImage
from bracket.models import Category

class ProductImageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = ProductImage
        fields = ["photo_url", "caption", "weight"]

    def get_photo_url(self, obj):
        return self.context.get('request').build_absolute_uri(obj.image.url)

class ProductAttributeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeItem
        fields = ["name", "selling_price", "quantity"]

class ProductAttributeSerializer(serializers.ModelSerializer):
    product_attribute_items = ProductAttributeItemSerializer(many=True, read_only=True)

    class Meta:
        model = ProductAttribute
        fields = ["name", "product_attribute_items"]

class ProductOptionSerializer(serializers.ModelSerializer):
    product_attribute = ProductAttributeSerializer()

    class Meta:
        model = ProductOption
        fields = ["product_attribute"]

class ProductSerialer(serializers.ModelSerializer):
    product_options = ProductOptionSerializer(many=True, read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "product_type",
            "base_price",
            "mrp",
            "selling_price",
            "is_active",
            "created_at",
            "modified_at",
            "product_options",
            "product_images"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerialer(many=True)
    
    class Meta:
        model = Category
        fields = '__all__'