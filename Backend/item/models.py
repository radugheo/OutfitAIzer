from constants import MAX_LENGTH
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=MAX_LENGTH)
    brand = models.CharField(max_length=MAX_LENGTH)
    color = models.CharField(max_length=MAX_LENGTH)
    image = models.ImageField(upload_to="clothes_pictures/")
    occasions = ArrayField(models.CharField(max_length=MAX_LENGTH))
