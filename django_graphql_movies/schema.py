from graphene import ObjectType, Schema
from movies import schema


class Query(schema.Query, ObjectType):
    pass


class Mutation(schema.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
