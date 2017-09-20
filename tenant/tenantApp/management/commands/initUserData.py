from django.contrib.auth.models import User
from django.core.management import BaseCommand, call_command

class Command(BaseCommand):
    help = "DEV COMMAND: loads data from the fixtures and sets the user passwords"

    def handle(self, *args, **options):
        #call_command('loaddata','data')
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()