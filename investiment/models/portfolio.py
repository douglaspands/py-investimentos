from typing import Self

from django.db import models

from core.models.base import BaseModel


class Portfolio(BaseModel):
    owner = models.ForeignKey("person.Person", on_delete=models.CASCADE)
    stocks = models.ManyToManyField(
        "investiment.StockPrice", through="PortfolioStockPrice"
    )

    def __str__(self: Self) -> str:
        return f"Portfolio of {self.owner.full_name}"
