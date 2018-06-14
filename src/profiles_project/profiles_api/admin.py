from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.UserProfile)
#Importamos admin y nuestro modelo de UserProfile
#para registrar un usuario de administrador
