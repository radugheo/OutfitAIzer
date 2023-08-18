import datetime

import jwt
from decouple import AutoConfig
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Response

from .models import Item
from .serializers import ItemSerializer
from .user.models import User

config = AutoConfig()


@api_view(["POST"])
def postItem(request):
    serializer = ItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def getAllItems(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")
    user = User.objects.filter(id=payload["id"]).first()
    items = Item.objects.filter(user=user)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
