import graphene
from data import users
from graphene import ObjectType


class Query(ObjectType):
    def resolve_user(self,info,id):
        return(list(filter(lambda  user: user["id"] == id)))[0]

    def resolve_users(self,info):
        return users