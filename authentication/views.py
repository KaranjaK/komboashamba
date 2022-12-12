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