from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from .serializers import (ResourceSerializer, CategorySerializer, TagSerializer, GroupSerializer)
from .permissions import IsAuthor
from links.models import Resource, Group, Tag, Category


class ResourceViewSet(viewsets.ModelViewSet):
    queryset=Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (IsAuthenticated, IsAuthor)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get',]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, IsAuthor)