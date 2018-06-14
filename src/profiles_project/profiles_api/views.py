from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """"Test API View."""

    def get(self, request, format=None):
        """Regresa una lista de caracterìsticas APIView"""

        #caracterìsticas que proporciona una API View
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'Is it similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        #Regresamos un objeto de respuesta en un diccionario que se
        #convierte a JSON
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
