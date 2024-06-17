from django.db import models

from core.models.base import BaseModel


class StockPrice(BaseModel):
    stock = models.ForeignKey("investiment.Stock", on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stock.ticker} price on {self.date}"
