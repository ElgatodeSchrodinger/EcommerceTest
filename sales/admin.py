from django.contrib import admin

# Register your models here.

from sales.models import Product, Category, Customer, SaleOrder, SaleOrderLine

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(SaleOrderLine)
@admin.register(SaleOrder)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('total_amount',)
    pass