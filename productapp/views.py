from django.shortcuts import render
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categoryapp.models import Category
from productapp.models import Product
from categoryapp.serializers import CategorySerializer
from productapp.serializers import ProductSerializer
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class ProductViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def get_product():
    print("Product list call")
    queryset = Product.objects.all()
    return ProductSerializer(queryset, many=True).data


# this api call every time get_product function
class CacheLessProductViewSet(APIView):
    def get(self, request,  *args, **kwargs):
        data = get_product()
        return Response(data=data, status=status.HTTP_200_OK)


# this api get product data from the cache
@cache_page(CACHE_TTL)
def product_view(request):
    return JsonResponse(get_product(), safe=False, status=200)