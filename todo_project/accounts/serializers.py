from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio']

# Serializer for registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            bio=validated_data.get('bio'),
        )
        return user