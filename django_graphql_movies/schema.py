import graphene
from movies import schema
from graphene_django.debug import DjangoDebug


class Query(schema.Query, graphene.ObjectType):
    # Debug field
    debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
