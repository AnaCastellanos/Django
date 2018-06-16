from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializer un campo de nombre para testear nuestra API View"""

    name = serializers.CharField(max_length=10)

#Estan diseñados para ser utilizados con modelos
#En este caso utilizar{a el model de Profile
class UserProfileSerializer(serializers.ModelSerializer):
    """Un serializer para nuestro objeto perfil de usuario."""

    #Metacase que le indica a Django que campos queremos
    #Usar de nuestro models
    class Meta:
        #Lo primo es el modelo al que se apunta
        model = models.UserProfile
        #Definimos que campos de este modelo queremos usar
        fields = ('id', 'email', 'name', 'password')
        #Define kwargs extra para propiedades.
        extra_kwargs = {'password': {'write_only': True}}

        #Función para manejar correctamente las contraseñas
        #Encripta la contraseña como un hash
        def create(self, validated_data):
            """Crea y regresa un nuevo usuario."""

            user = models.UserProfile(
                email = validated_data['email'],
                name = validated_data['name']
            )

            user.set_pasword(validated_data['password'])
            user.save()

            return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer para elementos de perfil."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

        #def create(self, validated_data):
