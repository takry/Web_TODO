from django.contrib.auth.models import User
from django.core.management import BaseCommand
from authapp.models import UserAuth, Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='nicolas', password='123', email='ad@mail.ru')
        data_user = {
            'username': 'Test',
            'first_name': 'Test_first',
            'last_name': 'Test_last',
            'email': '1@1.com'
        }
        user = UserAuth.objects.create(**data_user)
        data_project = {
            'name': 'Test',
            'url_repo': '1@github.com',
            'user': 'Test'
        }
        project = Project.objects.create(**data_project)
