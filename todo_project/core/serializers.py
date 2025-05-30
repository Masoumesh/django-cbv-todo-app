from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_done",
            "created_date",
            "updated_date",
            "user",
        ]
