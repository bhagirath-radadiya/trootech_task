from django.shortcuts import render
from rest_framework import mixins, generics, permissions, viewsets, status
from categoryapp.models import Category
from categoryapp.serializers import CategorySerializer, CategoryV2Serializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=['get'], name='hierarchical',
            url_path='hierarchical',
            url_name='hierarchical')
    def hierarchical(self, request, *args, **kwargs):

        queryset = Category.objects.filter(parent_category = None)

        serializer = CategoryV2Serializer(queryset, many=True)



        return Response(data=serializer.data, status=status.HTTP_200_OK)
