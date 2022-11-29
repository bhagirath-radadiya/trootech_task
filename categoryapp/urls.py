from django.urls import path, include
from rest_framework import routers
from categoryapp.views import CategoryViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]