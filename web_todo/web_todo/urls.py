"""web_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from authapp.views import UserAuthCustomViewSet, ProjectLimitOffsetPaginationViewSet
from todoapp.views import ToDoLimitOffsetPaginationViewSet

router = DefaultRouter()
router.register('userauth', UserAuthCustomViewSet)
router.register('todo', ToDoLimitOffsetPaginationViewSet)
router.register('project', ProjectLimitOffsetPaginationViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="TODO",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # re_path(r'^api/(?P<version>\d\.\d)/users/$', UserAuthCustomViewSet.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    re_path('swagger<str:format>/', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
    path("graphql/", GraphQLView.as_view(graphiql=True)),

    path("", TemplateView.as_view(template_name='index.html')),
    ]
