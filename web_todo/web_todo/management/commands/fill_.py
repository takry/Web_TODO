from django.core.management import BaseCommand

from authapp.models import UserAuth


class Command(BaseCommand):
    def handle(self, *args, **options):
        UserAuth.objects.create_superuser('admin', "admin@geekshop.ru", '123')
        UserAuth.objects.create_user('user1', "user1@geekshop.ru", '123')
        UserAuth.objects.create_user('user2', "user2@geekshop.ru", '123')
