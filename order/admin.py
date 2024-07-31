from django.contrib import admin
from .models import Order, Investment

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderId', 'type', 'amount','channel', 'status']
    list_filter = ['type', 'amount', 'status', 'channel']
    search_fields = ['orderId']

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ['orderId', 'plan', 'amount','status']
    list_filter = ['plan', 'amount', 'status']
    search_fields = ['orderId']

admin.site.register(Order, OrderAdmin)
admin.site.register(Investment, InvestmentAdmin)