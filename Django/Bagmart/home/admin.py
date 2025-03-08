from django.contrib import admin
from .models import UserProfile
from .models import Product
from .models import Bag
 
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'price', 'is_published', 'created_at') 
    list_display_links=('id', 'name')
    list_filter= ('price', 'created_at')
    list_editable = ('price','is_published')
    search_fields = ('name', 'price')
    ordering =('price',)
     
class BagAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'price', 'created_at') 
    list_display_links=('id', 'name')
    list_filter= ('price', 'created_at')
    list_editable = ('price',)
    search_fields = ('name', 'price')
    ordering =('price',)
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Product, ProductAdmin)
admin.site.register(Bag, BagAdmin)

