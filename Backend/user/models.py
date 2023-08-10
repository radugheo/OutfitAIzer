from constants import MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=MAX_LENGTH, unique=True)
    picture = models.ImageField(upload_to="user_pictures/")
    items = models.ManyToManyField("item.Item", blank=True)
    outfits = models.ManyToManyField("outfit.Outfit", blank=True)

    REQUIRED_FIELDS = ["email"]
