from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
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
    class Meta:
        model = Activity
        fields = '__all__'       
