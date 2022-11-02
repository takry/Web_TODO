import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from authapp.models import UserAuth, Project
from todoapp.models import ToDo


# class Query(ObjectType):
#     hello = graphene.String(default_value="Hi!")
# schema = graphene.Schema(query=Query)
#
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
# class Query(ObjectType):
#     all_projects = graphene.List(ProjectType)
#     def resolve_all_projects(root, info):
#         return Project.objects.all()
#
# schema = graphene.Schema(query=Query)
#
#
#
class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserAuthType(DjangoObjectType):
    class Meta:
        model = UserAuth
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(ObjectType):
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserAuthType)
    all_todo = graphene.List(ToDoType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return UserAuth.objects.all()

    def resolve_all_todo(root, info):
        return ToDo.objects.all()


schema = graphene.Schema(query=Query)
