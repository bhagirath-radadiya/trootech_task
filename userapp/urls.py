from django.urls import path, include
from rest_framework import routers
from userapp.views import SendEmailView


urlpatterns = [
    path('send-email/', SendEmailView.as_view()),
]