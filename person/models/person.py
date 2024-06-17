from typing import Self

from django.db import models

from core.models.base import BaseModel


class Person(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    @property
    def full_name(self: Self) -> str:
        return f"{self.first_name} {self.last_name}"
