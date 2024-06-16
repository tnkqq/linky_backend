from links.models import Resource, Group, Tag, Category
from rest_framework import serializers


class ResourceSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='email'
    )

    class Meta:
        fields = ('id', 'author', 'title', 'url', 'pub_datetime', 'group', 'category', 'tags')
        # read_only_fields = ('group',)
        model = Resource


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('slug',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'parent')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('slug',)