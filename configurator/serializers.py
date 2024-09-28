from rest_framework import serializers
from configurator.models import CPU

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'
