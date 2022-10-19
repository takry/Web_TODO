from django.test import TestCase

from rest_framework import status
from rest_framework.test import APISimpleTestCase, APIClient, APITestCase, APIRequestFactory, force_authenticate
from mixer.backend.django import mixer
from authapp.models import UserAuth
from authapp.views import UserAuthCustomViewSet, ProjectLimitOffsetPaginationViewSet
from todoapp.views import ToDoLimitOffsetPaginationViewSet
from .models import Project
from todoapp.models import ToDo


class Test_ToDoLimitOffsetPaginationViewSet(APITestCase):
    def setUp(self) -> None:
        django = UserAuth.objects.create_user(username='django', email='1@1.com', password='123')
        self.url = '/api/todo/'
        self.projects_dict = {'name': 'Test111', 'url_repo': '123@github.com', 'user': django}
        self.projects_dict_fake = {'name': 'Test_fake', 'url_repo': 'fake@github.com', 'user': django}
        self.format = 'json'
        self.username = 'admin'
        self.email = 'admin@mail.ru'
        self.password = 'admin_123'
        self.admin = UserAuth.objects.create_superuser(username=self.username, email=self.email, password=self.password)
        self.project = Project.objects.create(**self.projects_dict)
        self.project_fake = Project.objects.create(**self.projects_dict)
        self.todo_dict = {'project': self.project, 'text': 'Test', 'user': django}
        self.todo_dict_fake = {'project': self.project_fake.id, 'text': 'Test_fake', 'user': django}
        self.todo = ToDo.objects.create(**self.todo_dict)

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_test_case_update_admin(self):
        self.client.force_login(user=self.admin)
        response = self.client.put(f'{self.url}{self.todo.id}/', self.todo_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.todo.refresh_from_db()
        self.assertEqual(self.todo.project.id, self.projects_dict_fake.get('project'))
        self.assertEqual(self.todo.text, self.projects_dict_fake.get('text'))
        self.client.logout()


def tearDown(self) -> None:
    pass
