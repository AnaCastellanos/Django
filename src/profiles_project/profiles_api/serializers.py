from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer un campo de nombre para testear nuestra API View"""

    name = serializers.CharField(max_length=10)

    
