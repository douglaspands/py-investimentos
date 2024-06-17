from django.contrib import admin

from .models import Dividend, Portfolio, PortfolioStockPrice, Stock, StockPrice


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name")


@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ("stock", "date", "price")
    list_filter = ("stock", "date")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("owner",)
    # filter_horizontal = ("stocks",)


@admin.register(PortfolioStockPrice)
class PortfolioStockPriceAdmin(admin.ModelAdmin):
    list_display = ("portfolio", "stock_price", "shares")
    list_filter = ("portfolio",)


@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    list_display = ("stock", "amount", "date")
    list_filter = ("stock", "date")
