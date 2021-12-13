from django.shortcuts import render
from rest_framework import generics, status
from .models import Transaction, TransactionLineItemDetails, InventoryItem
from .serializers import TransactionSerializer, TransactionDetailSerializer, TransactionLineItemDetailsSerializer, InventoryItemSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .utils import set_tn_number

# Create your views here.
class TransactionList(generics.ListCreateAPIView):
    """
    Create and view transactions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            tn_number = serializer.set_tn_number()
            serializer.save(transaction_number=tn_number)
            message = {'message': "Transaction Created Successfully"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddLineItems(APIView):
    """
    Add line items to a transaction
    """
    serializer_class = TransactionLineItemDetailsSerializer
    def get(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
        except Exception as e:
            print(e)
            message = {'Message': 'Transaction with given id not found'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        line_items = TransactionLineItemDetails.objects.filter(transaction=id)
        serializer = TransactionLineItemDetailsSerializer(line_items, many=True)
        data = {'data': serializer.data}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
        except Exception as e:
            print(e)
            message = {'Message': 'Transaction with given id not found'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionLineItemDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            line_items = TransactionLineItemDetails.objects.filter(transaction=id)
            serializer = TransactionLineItemDetailsSerializer(line_items, many=True)
            data = {'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddInventoryItems(generics.ListCreateAPIView):
    """
    Add items to inventory
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class DeleteTransaction(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, retrieve and delete the data of a transaction
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class view_transaction(APIView):
    def get(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
        except Exception as e:
            print(e)
            message = {'Message': 'Transaction with given id not found'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = TransactionDetailSerializer(transaction)
        #data = {'data': tn_data}
        return Response(data.data, status=status.HTTP_200_OK)
