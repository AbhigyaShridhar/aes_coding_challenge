from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'transaction'

urlpatterns = [
    path('transactions/', views.TransactionList.as_view(), name="all_transactions"),
    path('transactions/view/line/<int:id>', views.AddLineItems.as_view(), name="add_line_item"),
    path('inventory/add', views.AddInventoryItems.as_view(), name="add_inventory_item"),
    path('transactions/edit/<int:pk>', views.DeleteTransaction.as_view(), name="edit_transactions"),
    path('transactions/details/<int:id>', views.view_transaction.as_view(), name="transaction_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
