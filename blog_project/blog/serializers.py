# blog/serializers.py
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):  # Note the correct class name
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(allow_null=True, required=False)
    video = serializers.FileField(allow_null=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'video', 'created_at', 'author']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

