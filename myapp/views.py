from django.shortcuts import render
from .models import Order, Client
import invoiced
from django.http import HttpResponse

INVOICE_NOT_SENT = 0
INVOICE_SENT = 1
PAYMENT_PENDING_SOON = 2
PAYMENT_RECEIVED = 3
STATUS_CHOICES = ((INVOICE_NOT_SENT, 'Invoice not sent'),(INVOICE_SENT, 'Invoice sent'), (PAYMENT_PENDING_SOON, 'Payment Pending Soon'), (PAYMENT_RECEIVED, 'Payment Received' ))

def index(request):
    clients = Client.objects.all()
    orders = Order.objects.all()
    for order in orders:
        # print(order.client.name)
        # print(order.client.email)
        # print(order.client.payment_type)
        # print(order.order_number)
        if order.invoice_checkbox is True:
            my_client = invoiced.Client("g7faIDdCVW7yByH09PR9oq18pBQNMgiL", True)
            # try:
            #     customer = my_client.Customer.retrieve(number=str(order.order_number))
            # except:
            customer = my_client.Customer.create(name=order.client.name, email=order.client.email, payment_terms = order.client.payment_type, number=str(order.order_number))
            my_items=[{'name': "HEYY", 'quantity':1, 'unit_cost': 20}, {'catalog_item': "delivery", 'quantity':1}]
            my_taxes=[{'amount': 3}]
            invoice = my_client.Invoice.create(customer=customer.id,payment_terms=order.client.payment_type, items=my_items, taxes=my_taxes)
            emails = invoice.send()
            order.status = INVOICE_SENT
        else:
            continue
    return HttpResponse("<h1>The invoices have been sent successfully!!</h1> ")
