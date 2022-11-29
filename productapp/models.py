from django.db import models
from categoryapp.models import Category


class Product(models.Model):
    name = models.CharField(max_length=128 ,null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='product_category')

    def __str__(self):
        return str(self.name)

    def get_category_list(self):
        return list(self.category.all().values_list('category', flat=True))
