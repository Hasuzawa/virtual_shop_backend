import graphene
from graphene_django import DjangoObjectType

from shop.models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"







class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product_by_id = graphene.Field(ProductType, id=graphene.String())

    def resolve_all_products(root, info):
        return Product.objects.all()

    
    def resolve_product_by_id(root, info, id):
        return Product.objects.get(pk=id)





schema = graphene.Schema(query=Query)