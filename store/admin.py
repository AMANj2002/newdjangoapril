from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.salesorder import SalesOrder
from .models.salesorder import OrderItem
from .models.retailstore import RetailStore


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'price']


# Register your models here.
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ['__str__', 'email']
    search_fields = ['first_name', 'last_name', 'email']


@admin.register(RetailStore)
class RetailStoreAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ['product', 'customer', 'price']
    search_fields = ['retail__name']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class SalesOrderAdmin(ImportExportModelAdmin):
    list_display = ('retail', 'date_ordered', 'complete')
    search_fields = ['retail__name']
    inlines = [OrderItemInline]


class OrderItemAdmin(ImportExportModelAdmin):
    list_display = ('order', 'product', 'qty')
    search_fields = ['order__retail__name', 'product__name']


admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
