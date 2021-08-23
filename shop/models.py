from django.db import models
#from models import F
#from django.db.models import Sum



class Product(models.Model):
    #id
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    #image = models.ImageField()

    short_description = models.CharField(max_length=64, blank=True)
    long_description = models.CharField(max_length=512, blank=True)

    unit_sold = models.IntegerField(blank=True, default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def income(self):
        return self.price * self.unit_sold      #for simplicity, assume permanently fixed pricing, i.e. no sales, discount

    def __str__(self):
        return f"{self.name}, {self.short_description}"


#singleton model for site statistics

""" class Shop(models.Model):

    @property
    def income(self):
        income = Product.objects.aggregate(Sum("income"))
    
    sold = models.BigIntegerField()
    

    def __str__(self):
        return "site-wide statistics such as total income and total units sold" """