from django.db import models


class Outfit(models.Model):
    items = models.ManyToManyField("item.Item", blank=True)
    rating = models.IntegerField()
    date = models.DateField()
