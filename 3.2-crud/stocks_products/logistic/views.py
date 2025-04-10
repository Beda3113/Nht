from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.prefetch_related('positions__product').all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['products']
    search_fields = ['positions__product__title', 'positions__product__description']
    pagination_class = LimitOffsetPagination
