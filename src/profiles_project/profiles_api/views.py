from django.shortcuts import render

#Para las API Viewsets
from rest_framework import viewsets
from rest_framework import status
#Para las APIView
from rest_framework.views import APIView
from rest_framework.response import Response
#token authentication integrado en rest_framework django
from rest_framework.authentication import TokenAuthentication
#Modulo de filtros agrega a nuestro viewset un filtro
from rest_framework import filters
#Para el inicio de sesion
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
#Da permisos si estas autenticado pero los restringe al acceso de solo lectura
#si no estan autenticados.
from rest_framework.permissions import IsAuthenticatedOrReadOnly


#Importa los serializers
from . import serializers
from . import models
#Para importar los permisos
from . import permissions



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

#Creamos una viewset
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Regresa una lista de objetos."""
        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Crea un nuevo objeto."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Helo {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Maneja los objetos por su ID's"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Actualiza el objeto"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Actualiza sólo una parte del objeto"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destruye/Elimina un objeto"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Crea y actualiza los perfiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_class = (TokenAuthentication,)
    #Clases de permisos aplicados a esta vista. La coma al final
    #Indica que es una tupla=Una lista no editable
    permission_classes = (permissions.UpdateOwnProfile,)
    #Filtros de busqueda
    filter_backends = (filters.SearchFilter,)
    #Definimos que filtros permitimos
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """Ingresa Email y pasword para regresar un token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Usa ObtainAuthToken APIView para validar y crear un token"""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Crea, lee y actuliza los elementos de perfil ."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    #Funcion para personalizar la logica de creacion de un objeto
    #a través de nuestro viewset
    def perform_create(self, serializer):
        """Envia al perfil de usuario que se logeo."""

        #Guarda en e serializer los datos.
        serializer.save(user_profile=self.request.user)
