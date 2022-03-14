from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Profile, Sports, Activity
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=User.objects.all(),
        slug_field="username",
    )
    class Meta:
        model = Activity
        fields = '__all__'       

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length = 32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        min_length = 8,
        max_length = 100,
        write_only = True
    )

    def create(self, validatedData):
        user = User(email=validatedData['email'], username=validatedData['username'])
        user.set_password(validatedData['password'])
        user.save()
        return user
        
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')