from django.contrib import admin
from .models import(Customer, OrderPlaced, Cart, Product)
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user' ,'name', 'locality','city', 'zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','selling_price','discounted_price','description','brand','category','product_Image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'customer','product','quantity','customer_info','product_info','ordered_date','status']
    def customer_info(self, obj):
        link = reverse('admin:app_customer_change',args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)
    def product_info(self, obj):
        link = reverse('admin:app_product_change',args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)