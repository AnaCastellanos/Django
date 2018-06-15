from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

#Importa los serializers
from . import serializers
from rest_framework import status

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
        return Response({'message': 'Hola!', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea un mensaje de bienvenida con nuestro nombre"""

        serializer = serializers.HelloSerializer(data=request.data)


        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #PK significa clave primaria a un objeto e especifico.
    def put(self, request, pk=None):
        """Maneja el actualizado de un objeto"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch sólo actualiza los campos requeridos."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Borra objetos"""

        return Response({'method': 'delete'})
