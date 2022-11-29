from django.shortcuts import render
from rest_framework import mixins, generics, permissions, viewsets
from categoryapp.models import Category
from productapp.models import Product
from categoryapp.serializers import CategorySerializer
from productapp.serializers import ProductSerializer


class ProductViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
