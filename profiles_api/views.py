from rest_ramework.views import APIView
from rest_ramework.views import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format = None):
        """returns a list of Apiview features"""
        an_apiview=[
             'Uses http methods as function (get ,post, put, patch ,delete)'
             'Is similar to a traditional django view'
             "Gives you the most control over your application logic"
             'is mapped manually to urls'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
