from rest_framework import serializers
from categoryapp.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent_category_name = serializers.SerializerMethodField('get_parent_category_name')

    class Meta:
        model = Category
        fields = ['id', 'category', 'parent_category', 'parent_category_name']
        extra_kwargs = {
            'parent_category_name': {'read_only': True}
        }

    def get_parent_category_name(self, obj):
        if obj.parent_category:
            return obj.parent_category.category
        else:
            return None