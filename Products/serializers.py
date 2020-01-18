from rest_framework import serializers
from Products.models import Products, Categories


class ProductsSerializer(serializers.ModelSerializer):

    quantity = serializers.IntegerField()
    price =  serializers.IntegerField()
    available = serializers.BooleanField()
    name = serializers.CharField()
    code = serializers.CharField()
    image = serializers.URLField()

    class Meta:
        model = Products
        fields = ('name','quantity', 'price', 'available', 'code', 'image')

class CategoriesSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    level = serializers.BooleanField()
    sub_level = serializers.BooleanField()
    sub_sub_level = serializers.BooleanField()
    sub_sub_sub_level = serializers.BooleanField()

    class Meta:
        model = Categories
        fields = ('name', 'level', 'sub_level', 'sub_sub_level', 'sub_sub_sub_level')