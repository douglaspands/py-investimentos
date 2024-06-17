from django.db import models

from core.models.base import BaseModel


class PortfolioStock(BaseModel):
    portfolio = models.ForeignKey("investiment.Portfolio", on_delete=models.CASCADE)
    stock = models.ForeignKey("investiment.Stock", on_delete=models.CASCADE)
    shares = models.PositiveIntegerField()
