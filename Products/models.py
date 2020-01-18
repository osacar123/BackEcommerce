# Django 
from django.db import models
# python 
import uuid

class Categories (models.Model):

    name = models.CharField(max_length=300, unique=True)
    level = models.IntegerField()
    sub_level = models.IntegerField()
    sub_sub_level = models.IntegerField()
    sub_sub_sub_level = models.IntegerField()

    class Meta:
        db_table = 'Categories'
        ordering = ['-id']
        verbose_name_plural = 'Categories'

class Products (models.Model):

    quantity = models.IntegerField()
    price =  models.IntegerField()
    available = models.BooleanField()
    sublevel_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, unique=False)
    code = models.CharField(max_length=300, unique=True)
    image = models.URLField()
	
    class Meta:
        db_table = 'Products'
        ordering = ['-id']
        verbose_name_plural = 'Products'