import graphene
from graphene import ObjectType


class User(ObjectType):
    id = graphene.String()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()