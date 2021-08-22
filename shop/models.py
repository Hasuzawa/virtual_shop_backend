from django.db import models


def Product(Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    #image = 
    short_description = models.CharField(max_length=64)
    long_description = models.CharField(max_length=512)
    unit_sold = models.IntegerField(default=0)
    date_published = models.DateTimeField("date published")


    def __str__(self):
        return self.name + self.short_description