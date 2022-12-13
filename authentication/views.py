from django.shortcuts import render
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User

MIN_LENGTH = 8

# Create your views here.
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            'min_length': f'Your Password has to be more that {MIN_LENGTH} characters!!'
        }
    )

    password2 = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            'min_length': f'Your Password has to be more that {MIN_LENGTH} characters!!'
        }
    )

    class META:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('The two passwords do not match!!')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            active = validated_data['active'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class USerViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer