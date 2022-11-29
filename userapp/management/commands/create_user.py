from django.core.management.base import BaseCommand
from userapp.models import CustomAdminUser


class Command(BaseCommand):
    help = 'Create bulk user'

    def add_arguments(self, parser):
        parser.add_argument('no_of_user', type=int, help='Number of users to be created')

        parser.add_argument('-u', '--username', type=str, help='Username prefix')

    def handle(self, *args, **kwargs):
        no_of_user = kwargs['no_of_user']
        username = kwargs['username']

        for i in range(no_of_user):
            if username:
                tmp = "{} {}".format(username, i+1)
            else:
                tmp = "person {}".format(i+1)
            obj, created = CustomAdminUser.objects.get_or_create(username=tmp)
            obj.custom_password = tmp
            obj.save()


# commands

# Arguments
# python manage.py create_user <Number of users which you want to create>

# Optional Arguments
# python manage.py create_user <Number of users which you want to create> -u <prefix username which you want>