from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions, generics



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['url', 'username', 'email', 'groups']
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name',]
