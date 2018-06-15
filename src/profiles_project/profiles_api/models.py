from django.db import models
#Importamos la base del modelo.
from django.contrib.auth.models import AbstractBaseUser
#Importamos la combinación de permisos
from django.contrib.auth.models import PermissionsMixin
#Importamos el administrador de objetos
from django.contrib.auth.models import BaseUserManager

#Administrador de objetos
class UserProfileManager(BaseUserManager):
    """ Ayuda a Django trabajar con nuestro modelo de usuario personalizado."""

    #Función que indica a Django no usar el modelo de usuario predeterminado.
    def create_user(self, email, name, password=None):
        """Crea un nuevo objeto de perfil de usuario."""

        #Nos aseguramos de que hayan ingresado un email, de lo contrario
        #regresamos un mensaje de error
        if not email:
            raise ValueError('Usuario debe tener un email adress.')

        #Normalizar la dirección de correo electrónico.
        email = self.normalize_email(email)
        #Crea un nuevo usuario con las reglas normalizadas
        user = self.model(email=email, name=name)

        #Para guardar la contraseña usamos esta función que nos ayuda a encriptar.
        user.set_password(password)
        #Guarda el usuario creado en la misma db creada con el administrador.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Crear y guardar un nuevo superusuario."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Representar un perfil de usuario dentro de nuestro sistema. """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #Refrencia del administrador de UserProfile
    objects = UserProfileManager()

    #Definimos el atributo username igual al email
    USERNAME_FIELD = 'email'
    #Campos requeridos
    REQUIRED_FIELDS = ['name']

    #Función de clase. Es requerida.
    def get_full_name(self):
        """Utilizado para obtener el nombre completo."""

        return self.name

    def get_short_name(self):
        """Utilizado para obtener un nombre corto."""

        return self.name

    #Función final. Es requerida. Devuelve el objeto en una cadena
    #Aquí indicamos que campos imprimir de UserProfile
    def __str__(self):
        """Django usa esto cuando necesita convertir el objeto a una cadena."""

        return self.email
