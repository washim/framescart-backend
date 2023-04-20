from django.db import models

class Customer(models.Model):
    name = models.CharField('Customer Name', max_length=255)
    mobile = models.CharField('Mobile', max_length=11, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    shipping_address = models.TextField('Shipping Address')
    city = models.CharField('City', max_length=30)
    state = models.CharField('State', max_length=30)
    pincode = models.CharField('Pincode', max_length=10)

    def __str__(self):
        return self.name