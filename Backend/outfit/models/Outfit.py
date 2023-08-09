from django.contrib.postgres.fields import ArrayField
from django.db import models
from item.models.Item import Item


class Outfit(models.Model):
    id = models.AutoField(primary_key=True)
    items = ArrayField(Item)
    rating = models.IntegerField()
    date = models.DateField()  # format-> YYYY-MM-DD
