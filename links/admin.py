from django.contrib import admin

from .models import Category, Group, Resource, Tag


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "category",
        "group",
        "url",
        "pub_datetime",
        "done_datetime",
    )

    search_fields = (
        "title",
        "url",
    )

    list_filter = ("pub_datetime", "done_datetime")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "pub_datetime",
        "parent",
        "is_publish",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "slug",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "slug",
    )
