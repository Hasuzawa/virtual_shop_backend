from django.contrib import admin
from django import forms
from .models import Product#, Shop


""" class ShopAdmin(admin.ModelAdmin):
    list_display = ("income", "sold")
    readonly_fields = ("income", "sold") """
    





class ProductModelForm(forms.ModelForm):
    long_description = forms.CharField(widget=forms.Textarea(attrs={"rows": 7, "cols": 150}))
    class Meta:
        fields = "__all__"
        model = Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description", "price", "unit_sold", "date_created", "last_modified", "income")
    list_filter = ("date_created", "last_modified")
    search_fields = ("name", "short_description", "long_description")
    #ordering = ("last_modified",)      // ordering is the active table order by default
    date_hierarchy = "last_modified"
    form = ProductModelForm


admin.site.register(Product, ProductAdmin)
""" admin.site.register(Shop) """
