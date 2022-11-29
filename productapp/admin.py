from django.contrib import admin
from productapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    ls = ['id', 'name', 'price', 'get_category_list']
    list_display = ls
    search_fields = ls


admin.site.register(Product, ProductAdmin)

