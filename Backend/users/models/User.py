from constants import MAX_LENGTH
from django.contrib.postgres.fields import ArrayField
from django.db import models
from items.models.Item import Item
from outfits.models.Outfit import Outfit


class User(models.Model):
    id = models.AutoField(primary_key=MAX_LENGTH)
    username = models.CharField(max_length=MAX_LENGTH)
    password = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH)
    picture = models.CharField()
    items = ArrayField(Item)
    outfits = ArrayField(Outfit)
