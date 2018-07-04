from django.contrib import admin
from .models import Order, Client

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'title', 'status', 'invoice_checkbox']
    list_filter = [ 'status', 'invoice_checkbox']
    list_editable = ['invoice_checkbox', ]

admin.site.register(Order, OrderAdmin)
admin.site.register(Client)
