from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_publish = models.BooleanField(default=True)
    pub_datetime = models.DateTimeField("Дата публикации", auto_now_add=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Category(models.Model):
    slug = models.CharField(max_length=20)

    def __str__(self):
        return self.slug


class Resource(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=80)

    url = models.URLField("Адрес ресурса")

    pub_datetime = models.DateTimeField("Дата публикации", auto_now_add=True)

    done_datetime = models.DateTimeField("Дата выполнения")

    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
    )

    Tag = models.ManyToManyField(
        Tag, blank=True, null=True
    )

    class Meta:
        ordering = ["-pub_datetime"]
        verbose_name = "Ресурс"
        verbose_name = "Ресурсы"
        default_related_name = "resources"
        default_related_name = "resources"

    def __str__(self):
        return f'{self.title}'


class TagResource(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag} {self.resource}'