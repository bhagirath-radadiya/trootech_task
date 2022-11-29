from django.urls import path, include
from rest_framework import routers
from userapp.views import SendEmailView, SendEmailAfter2MinView


urlpatterns = [
    path('send-email/', SendEmailView.as_view()),
    path('send-email-after-2-min/', SendEmailAfter2MinView.as_view()),
]