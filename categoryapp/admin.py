from django.contrib import admin
from categoryapp.models import Category


class CategoryAdmin(admin.ModelAdmin):
    ls = ['id', 'category', 'parent_category']
    list_display = ls
    search_fields = ls


admin.site.register(Category, CategoryAdmin)

