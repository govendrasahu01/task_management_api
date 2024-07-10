from rest_framework import serializers
from .models import *

class task_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        # fields = ['title','description']
        fields = "__all__"
    
    def validate(self, data):
        # Validation logic here
        return data   