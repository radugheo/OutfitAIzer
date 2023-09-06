import datetime

import jwt
from decouple import AutoConfig
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Response
from user.models import User

from .models import Outfit
from .serializers import OutfitSerializer

config = AutoConfig()


@api_view(["GET"])
def getOutfits(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")

    user = User.objects.filter(id=payload["id"]).first()
    outfits = user.outfits.all()
    serializer = OutfitSerializer(outfits, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def postRate(request, id):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")

    outfit = Outfit.objects.get(id=id)
    user = User.objects.filter(id=payload["id"]).first()

    if outfit not in user.outfits.all():
        response = {
            "message": "You are not allowed to rate this outfit!",
            "status": status.HTTP_401_UNAUTHORIZED,
        }
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)
    if not outfit:
        response = {
            "message": "Outfit does not exist!",
            "status": status.HTTP_404_NOT_FOUND,
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    if outfit.rating != 0:
        response = {
            "message": "You have already rated this outfit!",
            "status": status.HTTP_401_UNAUTHORIZED,
        }
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # get data from json request
        outfit.rating = request.data["rating"]
        outfit.save()
        response = {
            "message": "Rate successfully!",
            "status": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(["POST"])
def postOutfit(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")

    user = User.objects.filter(id=payload["id"]).first()
    serializer = OutfitSerializer(
        data=request.data
    )  # rating = 0 pentru inceput ca sa testez rateOutfit, date= "YYYY-MM-DD"
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user.outfits.add(serializer.data["id"])
    return Response(serializer.data)
