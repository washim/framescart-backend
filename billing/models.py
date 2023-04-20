from django.db import models

PAYMENT_STATUS = [
    ('inprogress', 'Inprogress'), 
    ('pending', 'Pending'), 
    ('canceled', 'Canceled'), 
    ('processing', 'Processing'), 
    ('Failed', 'Failed'), 
    ('completed', 'Completed'), 
    ('refund_requested', 'Refund Requested'), 
    ('refunded', 'Refunded')
]

SHIPPING_STATUS = [
    ('inprogress', 'Inprogress'),
    ('returning', 'Returning'),
    ('returned', 'Returned'),
    ('shipped', 'Shipped')
]

PAYMENT_MODE = [
    ('cod', 'Cash On Delivery'),
    ('money_transffer', 'Money Transffer'),
    ('online_payment', 'Online Payment')
]

class Invoice(models.Model):
    customer = models.ForeignKey("buyer.Customer", on_delete=models.CASCADE, related_name='invoices')
    total_due = models.FloatField(default=0.0)
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=50, default='cod')
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=50, default='inprogress')
    shipping_status = models.CharField(choices=SHIPPING_STATUS, max_length=50, default='inprogress')
    shipment_order_no = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField("Create Date", auto_now_add=True)
    modified_at = models.DateField("Modified Date", auto_now=True)

class StockIn(models.Model):
    product = models.ForeignKey("catalog.Product", related_name='stockin', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    notes = models.CharField(max_length=255, help_text="Put better notes for future refference." , default="")
    created_at = models.DateTimeField("Create Date", auto_now_add=True)
    modified_at = models.DateTimeField("Modified Date", auto_now=True)

class Stockout(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='stockouts')
    product = models.ForeignKey("catalog.Product", on_delete=models.CASCADE, related_name='+')
    product_attribute_item = models.TextField(blank=True, null=True)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    mrp = models.DecimalField(max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    ordered_quantity = models.IntegerField()