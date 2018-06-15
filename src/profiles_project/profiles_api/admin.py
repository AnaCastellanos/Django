from django.contrib import admin

from . import models

# Register your models here.

#Importamos admin y nuestro modelo de UserProfile
#para registrar un usuario de administrador
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
