from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Importa los serializers
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """"Test API View."""
    #variable serealizer que hace referencia a nuestro serializer.
    serializer_class = serializers.HelloSerializer

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

    def post(self, request):
        """Crea un mensaje de bienvenida con nuestro nombre"""
