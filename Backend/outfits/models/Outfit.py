from django.contrib.postgres.fields import ArrayField
from django.db import models
from items.models.Item import Item


class Outfit(models.Model):
    items = ArrayField(Item)
    rating = models.IntegerField()
    date = models.DateField()  # format-> YYYY-MM-DD
