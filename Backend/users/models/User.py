from django.contrib.postgres.fields import ArrayField
from django.db import models
from items.models.Item import Item
from outfits.models.Outfit import Outfit


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    picture = models.CharField()
    items = ArrayField(Item)
    outfits = ArrayField(Outfit)
