from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sales.models import (
    Product,
    Customer,
    Category,
    SaleOrder,
    SaleOrderLine,
)

from sales.serializers import (
    ProductSerializer,
    CustomerSerializer,
    CategorySerializer,
    SaleOrderSerializer,
    SaleOrderLineSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET'])
def detail_category(request):
    """
    List Category.

    Sort values:
    - Best Seller: sale
    - Price: price
    - Name: name
    """

    categ_id = request.query_params.get('id', None)
    sort_by = request.query_params.get('sort_by', None)

    category = Category.objects.get(pk=categ_id)
    category_details = CategorySerializer(category).data

    if categ_id is not None and sort_by is not None:

        products = Product.objects.filter(categ_id=categ_id)

        if products:
            products = ProductSerializer(products, many=True).data
            print(products)
            order_product_ids = []

            if products:
                if sort_by == 'sale':
                    order_product_ids = sorted(products, key=lambda prod: prod['quantitysold'])
                elif sort_by == 'price':
                    order_product_ids = sorted(products, key=lambda prod: prod['price'])
                elif sort_by == 'name':
                    order_product_ids = sorted(products, key=lambda prod: prod['name'])

            category_details['products'] = order_product_ids

    return Response(category_details)

@api_view(['POST'])
def add_to_cart(request):
    """
    Add to cart
    """
    order_id = request.query_params.get('id', None)
    product_id = request.query_params.get('product', None)
    quantity = request.query_params.get('quantity', None)

    line = {
        'product_id': product_id,
        'quantity': quantity,
    }

    if order_id is not None:
        line['order_id'] = order_id
    else:
        default_order = SaleOrderSerializer(data={})
        if default_order.is_valid():
            default_order.save()
            print(default_order.data)
            line['order_id'] = default_order.data['id']

    line_obj = SaleOrderLineSerializer(data=line)
    if line_obj.is_valid():
        line_obj.save()

    return Response(line_obj.data)

@api_view(['GET'])
def cart(request):
    """
     Cart Detail.
    """
    order_id = request.query_params.get('id', None)

    order_data = []

    if order_id is not None:
        order = SaleOrder.objects.get(pk=order_id)
        # print(order)
        order_data = SaleOrderSerializer(order).data
        # print(order_data)
        lines = SaleOrderLine.objects.filter(order_id=order_id)
        lines_data = SaleOrderLineSerializer(lines, many=True).data

        order_data['lines'] = lines_data

    return Response(order_data)

@api_view(['PUT'])
def sale(request):
    """
    Process cart.
    """

    order_id = request.query_params.get('id', None)

    if order_id is not None:
        order = SaleOrder.objects.get(pk=order_id)
        order_data = SaleOrderSerializer(order, data={'state': 'process'})

        if order_data.is_valid():
            order_data.save()
            return Response({'message': 'Se proceso la compra'})

    return Response({'message': 'Error al realizar su compra'})