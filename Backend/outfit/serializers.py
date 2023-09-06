import datetime

from rest_framework import serializers

from .models import Outfit


class OutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outfit
        fields = ["id", "items", "rating", "date"]
