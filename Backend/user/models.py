import os

from constants import MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    return os.path.join(f"profile_pictures/{instance.username}/", filename)


class User(AbstractUser):
    email = models.EmailField(max_length=MAX_LENGTH, unique=True)
    picture = models.ImageField(upload_to=user_directory_path)
    items = models.ManyToManyField("item.Item", blank=True)
    outfits = models.ManyToManyField("outfit.Outfit", blank=True)

    REQUIRED_FIELDS = ["email"]
