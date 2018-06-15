from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Permite a los usuarios editar su propio perfil"""

    def has_object_permission(self, request, view, obj):
        """Checar si un usuario trata de editar su perfil."""

        #Si el método requerido esta dentro de los métodos seguros.
        if request.method in permissions.SAFE_METHODS:
            return True

        #Si el usuario esta intenatando actualizar su perfil
        #es decir, no hizo un método seguro (GET) sino un POST, PUT
        #DELETE. Se asegura que el usuario sea el mismo que el que
        #esta utenticado y del perfil que intenta editar.
        return obj.id == request.user.id
