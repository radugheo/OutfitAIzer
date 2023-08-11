from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def getRoutes(request):
    test = {
        "primulCamp": "primul camp",
        "alDoileaCamp": "al doilea camp",
        "alTreileaCamp": "al treilea camp",
    }

    return Response(test)
