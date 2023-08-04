from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def getRoutes(request, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    test = {
        "primulCamp": "primul camp",
        "alDoileaCamp": "al doilea camp",
        "alTreileaCamp": "al treilea camp",
    }
    return Response(test)
