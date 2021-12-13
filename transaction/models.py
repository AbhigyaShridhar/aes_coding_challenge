from django.db import models
from datetime import time, datetime

# Masters required in transaction models
class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.short_name


class DepartmentMaster(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class CompanyLedgerMaster(models.Model):
    name = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class ArticleMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
PENDING = 'PENDING'
COMPLETED = 'COMPLETED'
CLOSE = 'CLOSE'
TRANSACTION_CHOICES = (
    (PENDING, 'PENDING'),
    (COMPLETED, 'COMPLETED'),
    (CLOSE, 'CLOSE')
)

class Transaction(models.Model):
    tn_time = models.DateTimeField(auto_now_add=True, null=True)
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.PROTECT)
    branch = models.ForeignKey(BranchMaster, on_delete=models.PROTECT)
    department = models.ForeignKey(DepartmentMaster, on_delete=models.PROTECT)
    transaction_number = models.CharField(max_length=100, unique=True)
    transaction_status = models.CharField(max_length=9, choices=TRANSACTION_CHOICES, default=PENDING)
    remarks = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.transaction_number

KG = 'KG'
METER = 'METER'
UNIT_CHOICES = {
    (KG, 'KG'),
    (METER, 'METER')
}

class TransactionLineItemDetails(models.Model):
     inventory_items = models.ManyToManyField("InventoryItem")
     transaction = models.ForeignKey(Transaction,on_delete=models.PROTECT, related_name="line_items")
     article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
     colour = models.ForeignKey(ColorMaster, on_delete=models.PROTECT)
     required_on = models.DateTimeField(default=datetime.now())
     quantity = models.FloatField(default=0)
     rate = models.PositiveIntegerField(default=0)
     unit = models.CharField(max_length=5, choices=UNIT_CHOICES, default=KG)

     class Meta:
         unique_together = [['transaction', 'article', 'colour']]

class InventoryItem(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    colour = models.ForeignKey(ColorMaster, on_delete=models.PROTECT)
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.PROTECT)
    gross = models.FloatField(default=0)
    net = models.FloatField(default=0)
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES, default=KG)
