import datetime

import jwt
from decouple import AutoConfig
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Response

from .models import User
from .serializers import UserSerializer

config = AutoConfig()


@api_view(["POST"])
def postLogin(request):
    user_username = request.data["username"]
    user_password = request.data["password"]

    user = User.objects.filter(username=user_username).first()

    if user is None:
        raise AuthenticationFailed("User not found!")
    if not user.check_password(user_password):
        raise AuthenticationFailed("Incorrect password!")

    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, config("DJANGO_JWT_SECRET"), algorithm="HS256")
    response = Response()
    response.set_cookie(key="jwt", value=token, httponly=True)
    response.data = {"jwt": token}
    return response


@api_view(["GET"])
def getUser(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")
    user = User.objects.filter(id=payload["id"]).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def getLogout(request):
    response = Response()
    response.delete_cookie("jwt")
    response.data = {"message": "success"}
    return response


@api_view(["POST"])
def postRegister(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["PATCH"])
def patchUpdate(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Not authenticated!")
    else:
        try:
            payload = jwt.decode(
                token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET"])
def getDeleteLogged(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Not authenticated!")
    else:
        try:
            payload = jwt.decode(
                token, config("DJANGO_JWT_SECRET"), algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        user = User.objects.filter(id=payload["id"]).first()
        user.delete()
        response = {
            "message": "User successfully deleted!",
            "status": status.HTTP_200_OK,
        }
        return Response(response)


@api_view(["POST"])
def postDelete(request, id):
    user = User.objects.filter(id=id).first()
    if not user:
        response = {
            "message": "User not found!",
            "status": status.HTTP_404_NOT_FOUND,
        }
        return Response(response)

    user.delete()
    response = {
        "message": "User successfully deleted!",
        "status": status.HTTP_200_OK,
    }
    return Response(response)
