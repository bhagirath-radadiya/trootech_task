from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userapp.models import CustomAdminUser
from userapp.tasks import send_email_celery, send_email_after_2_min_celery
from datetime import datetime, timedelta


class SendEmailView(APIView):

    def post(self, request,  *args, **kwargs):
        send_email_celery.delay(request.data)
        return Response(status=status.HTTP_200_OK)

class SendEmailAfter2MinView(APIView):

    def post(self, request,  *args, **kwargs):
        send_email_after_2_min_celery.delay(request.data)
        return Response(status=status.HTTP_200_OK)