from api.models.Item import Item
from api.models.Outfit import Outfit
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(models.Model):
    ussername = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    picture = models.CharField()
    items = ArrayField(Item)
    outfits = ArrayField(Outfit)
