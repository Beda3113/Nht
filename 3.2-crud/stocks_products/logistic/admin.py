from django.contrib import admin
from .models import Product, Stock, StockProduct

class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1  
    min_num = 1  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('title',)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
    list_display_links = ('id', 'address')
    search_fields = ('address',)
    inlines = [StockProductInline]  


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock', 'product', 'quantity', 'price')
    list_display_links = ('id',)
    list_filter = ('stock', 'product')
    search_fields = ('product__title', 'stock__address')
