from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a liat of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, delete, put)',
            'Is similar to traditional Django views',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})

    
    def post(self, request):
        """Create a Hello world with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({"message": f"Hello {name}"})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )