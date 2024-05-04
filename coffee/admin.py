from django.contrib import admin
from .models import CartItem
class CoffeeAdmin(admin.ModelAdmin):
    list_display =('product_name', 'product_price', 'quantity')
# Register your models here.
admin.site.register(CartItem)