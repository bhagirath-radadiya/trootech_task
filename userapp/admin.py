from django.contrib import admin
from userapp.models import CustomAdminUser


class CustomAdminUserAdmin(admin.ModelAdmin):
    ls = ['id', 'username', 'custom_password', 'is_superuser', 'is_staff', 'is_active']
    list_display = ls
    search_fields = ls


admin.site.register(CustomAdminUser, CustomAdminUserAdmin)
