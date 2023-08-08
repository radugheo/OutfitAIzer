from api.models.Item import Item
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Outfit(models.Model):
    items = ArrayField(Item)
    rating = models.IntegerField()
    date = models.DateField()  # format-> YYYY-MM-DD
