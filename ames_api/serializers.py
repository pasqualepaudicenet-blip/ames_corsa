from rest_framework import serializers
from .models import CustomUser, Corsa, Sample

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']



class SampleCorsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['sampleId', 'sampleName']

class CorsaSerializer(serializers.ModelSerializer):
    samples = SampleCorsaSerializer(many=True, read_only=True)

    class Meta:
        model = Corsa
        fields = [
            'pk',
            'date', 
            'description', 
            'type', 
            'derivatiopn_path',
            'samples'
                ]
class CorsaSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corsa
        fields = [
            'date', 
            'description', 
            'type', 
            'derivatiopn_path',
                ]

class SampleSerializer(serializers.ModelSerializer):
    corsa = CorsaSampleSerializer(read_only=True)

    class Meta:
        model = Sample
        fields = [
            'sampleId', 
            'sampleName', 
            'corsa'
            ]
        