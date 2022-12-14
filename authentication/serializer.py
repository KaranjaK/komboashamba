from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers
from authentication.models import Profile


MIN_LENGTH = 8    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = 'username','email', 'first_name','last_name', 'password','password2','phone_number'

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
        )
        user.set_password(validated_data['password'])
        user.save()

        return user