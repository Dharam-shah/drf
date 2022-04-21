from rest_framework import serializers
from .models import TodoApp

class TodoAppSearilizers(serializers.ModelSerializer):
    class Meta:
        model = TodoApp
        fields = ['id', 'task_name', 'image', 'task_created', 'dead_line', 'task_completed']