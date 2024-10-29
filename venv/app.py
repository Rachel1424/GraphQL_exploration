from dataclasses import Field
import graphene
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User
from graphene import String,Field,List

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delte_user = DeleteUser.Field()

class MyQuery(Query):
    user = Field(User)
    get_user = Field(User,id = String())
    get_users= List(User)

schema = graphene.Schema(query = MyQuery, mutation = MyMutations)

result = schema.execute(
    '''
    mutation {
        createUser(id:"2", name: "Jane Doe", email:"non@real.com", password: "123456"){
            user {
            id
            name
            email
            password
           }  
        }
     }
     
    '''
)
print(result.data)