from django.shortcuts import render
from rest_framework import mixins, generics, permissions, viewsets
from categoryapp.models import Category
from categoryapp.serializers import CategorySerializer


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
