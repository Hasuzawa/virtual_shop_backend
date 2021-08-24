import graphene
from graphene_django import DjangoObjectType

from shop.models import Product

#queries

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"

#mutations

class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        change = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls, root, into, id, change):
        product = Product.objects.get(pk=id)
        product.unit_sold += change
        product.save()
        return UpdateProduct(product=product)


    



#query

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product_by_id = graphene.Field(ProductType, id=graphene.Int(required=True))

    def resolve_all_products(root, info):
        return Product.objects.all()

    
    def resolve_product_by_id(root, info, id):
        return Product.objects.get(pk=id)
        #return null if product with that id does not exist

#mutation

class Mutation(graphene.ObjectType):
    update_product = UpdateProduct.Field()

#schema

schema = graphene.Schema(query=Query, mutation=Mutation)