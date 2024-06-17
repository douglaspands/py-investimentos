from django.db import models

from core.models.base import BaseModel


class Dividend(BaseModel):
    stock = models.ForeignKey("investiment.Stock", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Dividend {self.amount} for {self.stock.ticker}"
