from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=128 ,null=True, blank=True)
    parent_category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True, related_name="category_parent_category")

    def __str__(self):
        return str(self.category)
