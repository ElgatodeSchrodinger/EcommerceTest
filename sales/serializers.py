from rest_framework import serializers
from sales.models import (
    Product,
    Customer,
    Category,
    SaleOrder,
    SaleOrderLine,
)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'categ_id', 'name', 'image', 'price', 'stock', 'quantitysold']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = ['id', 'created_date', 'state', 'customer', 'total_amount']


class SaleOrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderLine
        fields = ['id', 'order_id', 'product_id', 'quantity']
