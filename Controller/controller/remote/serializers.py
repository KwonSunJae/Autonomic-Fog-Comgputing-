from rest_framework import serializers
from .models import Remote, ModuleField

class RemoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remote
        fields = '__all__'
        
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleField
        fields = '__all__'