from django.contrib.postgres.fields import ArrayField
from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.CharField()
    occasions = ArrayField(models.CharField(max_length=50))
