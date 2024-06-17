from django.db import models

from core.models.base import BaseModel


class Stock(BaseModel):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.ticker
