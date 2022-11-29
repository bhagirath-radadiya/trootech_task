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


class CategoryV2Serializer(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField('get_sub_category')

    class Meta:
        model = Category
        fields = ['id', 'category', 'sub_category']
        extra_kwargs = {
            'sub_category': {'read_only': True}
        }

    def get_sub_category(self, obj):
        queryset = obj.category_parent_category.all()
        if queryset:
            return CategoryV2Serializer(queryset, many=True).data
        else:
            return None