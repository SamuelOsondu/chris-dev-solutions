from rest_framework import serializers
from .models import Country, State, Tribe, BlogPost, Comment


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class TribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribe
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog_post', 'author_name', 'text', 'created_at']


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'image', 'content', 'created_at', 'updated_at', 'country', 'state', 'tribe', 'comments']
