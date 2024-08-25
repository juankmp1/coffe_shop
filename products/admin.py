from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name','description','price','available','photo']
    search_fields = ['name','description','price','available']
    
admin.site.register(Product, ProductAdmin)
