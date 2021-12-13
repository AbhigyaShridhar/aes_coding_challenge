from rest_framework import serializers
from .models import Transaction, TransactionLineItemDetails, InventoryItem
from datetime import time, datetime

class TransactionSerializer(serializers.ModelSerializer):
    line_items = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField()
    branch = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = ['id', 'company', 'branch', 'department', 'transaction_number', 'line_items', 'transaction_status', 'remarks']
        extra_kwargs = {'tn_time': {'write_only': True}}
        read_only_fields = ['id', 'transaction_number']

    def set_tn_number(self):
        tn_number = "TRN"
        year = datetime.now().year
        count = Transaction.objects.filter(tn_time__year=year).count() + 1
        tn_number = tn_number + "/" + str(year) + "/" + str(count)
        return tn_number

        """
        def create(self, validated_data):
            transaction = Transaction(
                company=validated_data['company'],
                branch=validated_data['branch'],
                department=validated_data['department'],
                transaction_number=set_tn_number(),
                transaction_status=validated_data['transaction_status'],
                remarks=validated_data['remarks']
            )
            transaction.save()
            return transaction
        """

class TransactionLineItemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLineItemDetails
        fields = ['id', 'transaction', 'inventory_items', 'article', 'colour', 'required_on', 'quantity', 'rate', 'unit']
        read_only_fields = ['id']

        def create(self, validated_data):
            return TransactionLineItemDetails.objects.create(**validated_data)

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class TransactionLineItemDetailsSerializerWithInventory(serializers.ModelSerializer):
    inventory_items = InventoryItemSerializer(many=True)

    class Meta:
        model=TransactionLineItemDetails
        fields = '__all__'

class TransactionDetailSerializer(serializers.ModelSerializer):
    line_items = TransactionLineItemDetailsSerializerWithInventory(many=True)

    class Meta:
        model = Transaction
        fields = '__all__'
