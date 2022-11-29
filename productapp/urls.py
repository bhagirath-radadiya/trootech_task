from django.urls import path, include
from rest_framework import routers
from productapp.views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]