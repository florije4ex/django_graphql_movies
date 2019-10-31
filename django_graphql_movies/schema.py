from graphene import ObjectType, Schema, Field
from movies import schema
from graphene_django.debug import DjangoDebug


class Query(schema.Query, ObjectType):
    debug = Field(DjangoDebug, name='_debug')


class Mutation(schema.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
