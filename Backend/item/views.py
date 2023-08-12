from rest_framework.decorators import api_view
from rest_framework.views import Response

from .serializers import ItemSerializer


@api_view(["POST"])
def postItem(request):
    serializer = ItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
