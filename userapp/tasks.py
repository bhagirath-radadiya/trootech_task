from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
import xlwt
from io import BytesIO
from userapp.models import CustomAdminUser
import time


@shared_task
def send_email_celery(data):
    email = data.get('email')

    queryset = CustomAdminUser.objects.filter(is_superuser=False)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['id','username']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = queryset.values_list("id","username")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    output = BytesIO()
    wb.save(output)

    subject = 'User data'
    message = f'Hi {email}, Here we attached user data.'
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    mail.attach('export_file.xlsb', output.getvalue(), 'application/ms-excel')
    mail.send()


@shared_task
def send_email_after_2_min_celery(data):
    time.sleep(120)

    email = data.get('email')

    queryset = CustomAdminUser.objects.filter(is_superuser=False)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['id','username']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = queryset.values_list("id","username")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    output = BytesIO()
    wb.save(output)

    subject = 'User data'
    message = f'Hi {email}, Here we attached user data.'
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    mail.attach('export_file.xlsb', output.getvalue(), 'application/ms-excel')
    mail.send()
