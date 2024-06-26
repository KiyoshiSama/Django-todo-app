from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','user','title','is_done','created']