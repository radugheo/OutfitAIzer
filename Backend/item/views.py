import datetime

import jwt
from decouple import AutoConfig
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Response
from user.models import User

from .models import Item
from .serializers import ItemSerializer

config = AutoConfig()


@api_view(["POST"])
def postItem(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")
    serializer = ItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = User.objects.filter(id=payload["id"]).first()
    user.items.add(serializer.data["id"])
    return Response(serializer.data)


@api_view(["GET"])
def getItems(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")
    user = User.objects.filter(id=payload["id"]).first()
    items = user.items.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def postDelete(request, id):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")

    item = Item.objects.get(id=id)
    user = User.objects.filter(id=payload["id"]).first()

    if item not in user.items.all():
        response = {
            "message": "You are not allowed to delete this item!",
            "status": status.HTTP_401_UNAUTHORIZED,
        }
        return Response(response)

    if not item:
        response = {
            "message": "Item not found!",
            "status": status.HTTP_404_NOT_FOUND,
        }
        return Response(response)

    response = {
        "message": "Item successfully deleted!",
        "status": status.HTTP_200_OK,
    }
    item.delete()
    return Response(response)
