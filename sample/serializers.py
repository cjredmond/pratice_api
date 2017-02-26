from rest_framework import serializers
from sample.models import Person, FreeAgent, PackersPlayer

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class FreeAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeAgent
        fields = '__all__'


class PackersPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackersPlayer
        fields = '__all__'
