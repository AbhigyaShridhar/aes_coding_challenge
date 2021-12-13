from django.contrib import admin
from .models import *

# register your models here.
admin.site.register(BranchMaster)
admin.site.register(DepartmentMaster)
admin.site.register(CompanyLedgerMaster)
admin.site.register(ArticleMaster)
admin.site.register(ColorMaster)
admin.site.register(Transaction)
admin.site.register(TransactionLineItemDetails)
admin.site.register(InventoryItem)
