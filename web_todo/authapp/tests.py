from django.test import TestCase

from rest_framework import status
from rest_framework.test import APISimpleTestCase, APIClient, APITestCase, APIRequestFactory, force_authenticate
from mixer.backend.django import mixer
from authapp.models import UserAuth
from authapp.views import UserAuthCustomViewSet, ProjectLimitOffsetPaginationViewSet
from todoapp.views import ToDoLimitOffsetPaginationViewSet
from .models import Project


class TestProjectLimitOffsetPaginationViewSet(TestCase):

    def setUp(self) -> None:
        django = UserAuth.objects.create_user(username='django', email='1@1.com', password='123')
        self.url = '/api/project/'
        self.projects_dict = {'name': 'Test111', 'url_repo': '123@github.com', 'user': django}
        self.projects_dict_fake = {'name': 'Test_fake', 'url_repo': 'fake@github.com', 'user': django}
        self.format = 'json'
        self.username = 'admin'
        self.email = 'admin@mail.ru'
        self.password = 'admin_123'
        self.admin = UserAuth.objects.create_superuser(username=self.username, email=self.email, password=self.password)
        self.project = Project.objects.create(**self.projects_dict)

    def test_factory_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectLimitOffsetPaginationViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_factory_create_guest(self):
    #     factory = APIRequestFactory()
    #     request = factory.post(self.url, self.projects_dict, format=self.format)
    #     view = ProjectLimitOffsetPaginationViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #
    # def test_factory_create_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post(self.url, self.projects_dict, format=self.format)
    #     force_authenticate(request, self.admin)
    #     view = ProjectLimitOffsetPaginationViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_client_detail(self):
        client = APIClient()
        response = client.get(f'{self.url}{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_client_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.project.id}/', **self.projects_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_api_client_update_admin(self):
    #     client = APIClient()
    #     client.force_authenticate(user=self.admin)
    #     response = client.put(f'{self.url}{self.project.id}/', data=self.projects_dict_fake)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     self.project.refresh_from_db()
    #     self.assertEqual(self.project.name, self.projects_dict_fake.get('name'))
    #     self.assertEqual(self.project.url_repo, self.projects_dict_fake.get('url_repo'))
    #     self.assertEqual(self.project.user, self.projects_dict_fake.get('user'))
    #     client.logout()

    def tearDown(self) -> None:
        pass
