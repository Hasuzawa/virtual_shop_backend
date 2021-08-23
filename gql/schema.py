import graphene
from graphene_django import DjangoObjectType

from shop.models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"







class Query(graphene.ObjectType):
    pass
