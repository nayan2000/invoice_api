from django.db import models
from django.core.validators import RegexValidator

INVOICE_NOT_SENT = 0
INVOICE_SENT = 1
PAYMENT_PENDING_SOON = 2
PAYMENT_RECEIVED = 3

NET_7 = 0
NET_14 = 1
NET_22 = 2
NET_30 = 3

INDIVIDUAL = 0
COMPANY = 1

STATUS_CHOICES = ((INVOICE_NOT_SENT, 'Invoice not sent'),(INVOICE_SENT, 'Invoice sent'), (PAYMENT_PENDING_SOON, 'Payment Pending Soon'), (PAYMENT_RECEIVED, 'Payment Received' ))
PAYMENT_TYPE_CHOICES = ((NET_7, 'NET 7'), (NET_14, 'NET 14'), (NET_22, 'NET 22'), (NET_30, 'NET 30'))
CLIENT_TYPE_CHOICES = ((INDIVIDUAL, 'Individual'), (COMPANY, 'Company'))
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Client(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100, unique=True)
    payment_type = models.SmallIntegerField(choices=PAYMENT_TYPE_CHOICES)
    client_type = models.SmallIntegerField(choices=CLIENT_TYPE_CHOICES)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        detail = self.name
        return detail

    def get_payment_type(self):
        return PAYMENT_TYPE_CHOICES[self.payment_type][1]

    def client_type(self):
        return CLIENT_TYPE_CHOICES[self.client_type][1]

class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE )
    order_number = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200, default='')
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
    invoice_checkbox = models.BooleanField()

    def __str__(self):
        detail = str(self.order_number) + '->' + self.title
        return detail

    def get_order_status(self):
        return STATUS_CHOICES[self.status][1]
