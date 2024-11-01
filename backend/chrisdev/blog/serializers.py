from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = "__all__"
        # fields = ('id', 'title', 'image', 'author', 'content', 'created_at', 'updated_at')
