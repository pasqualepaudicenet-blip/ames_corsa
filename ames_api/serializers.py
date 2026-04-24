from rest_framework import serializers
from .models import CustomUser, Corsa, Sample
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'is_superuser']

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class SampleCorsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['sample_id', 'sample_name']

class CorsaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Corsa
        fields = [
            'pk',
            'date', 
            'description', 
            'type', 
            'derivation_path',
                ]
        
class CorsaDetailSerializer(serializers.ModelSerializer):
    samples = SampleCorsaSerializer(many=True, read_only=True)

    class Meta:
        model = Corsa
        fields = [
            'pk',
            'date',
            'description',
            'type',
            'derivation_path',
            'samples'
        ]

class CorsaSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corsa
        fields = [
            'date', 
            'description', 
            'type', 
            'derivation_path',
                ]

class SampleSerializer(serializers.ModelSerializer):
    corsa = CorsaSampleSerializer(read_only=True)

    class Meta:
        model = Sample
        fields = [
            'sample_id', 
            'sample_name', 
            'corsa'
            ]
        