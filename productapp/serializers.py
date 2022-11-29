from rest_framework import serializers
from categoryapp.models import Category
from productapp.models import Product
from categoryapp.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category_list = serializers.SerializerMethodField('get_category_list')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'category_list']
        extra_kwargs = {
            'category': {'write_only': True},
            'category_list': {'read_only': True}
        }

    def get_category_list(self, obj):
        queryset = obj.category.all()
        return CategorySerializer(queryset, many=True).data
