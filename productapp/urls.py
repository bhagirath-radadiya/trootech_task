from django.urls import path, include
from rest_framework import routers
from productapp.views import ProductViewSet, CacheLessProductViewSet, product_view

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-list/', CacheLessProductViewSet.as_view()),
    path('cache-product-list/', product_view),
]