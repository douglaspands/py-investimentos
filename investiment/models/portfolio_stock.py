from django.db import models

from core.models.base import BaseModel


class PortfolioStockPrice(BaseModel):
    portfolio = models.ForeignKey("investiment.Portfolio", on_delete=models.CASCADE)
    stock_price = models.ForeignKey("investiment.StockPrice", on_delete=models.CASCADE)
    shares = models.PositiveIntegerField()
