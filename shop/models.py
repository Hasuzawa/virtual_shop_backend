from django.db import models


class Product(models.Model):
    #id
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    image = models.ImageField()

    short_description = models.CharField(max_length=64)
    long_description = models.CharField(max_length=1024)
    
    unit_sold = models.IntegerField(blank=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + self.short_description