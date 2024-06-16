from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(verbose_name="Заголовок группы", max_length=80)
    author = models.ForeignKey(
        User, verbose_name="Автор группы", on_delete=models.CASCADE
    )
    is_publish = models.BooleanField("Статус выполнения", default=True)
    pub_datetime = models.DateTimeField("Дата публикации", auto_now_add=True)
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Tag(models.Model):
    slug = models.SlugField()

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.slug


class Category(models.Model):
    slug = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.slug


class Resource(models.Model):

    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)

    title = models.CharField(verbose_name="Заголовок", max_length=80)

    url = models.URLField("Адрес ресурса")

    pub_datetime = models.DateTimeField("Дата публикации", auto_now_add=True)

    done_datetime = models.DateTimeField("Дата выполнения", blank=True, null=True)

    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    Tag = models.ManyToManyField(Tag, blank=True, null=True)

    class Meta:
        ordering = ["-pub_datetime"]
        verbose_name = "Ресурс"
        verbose_name_plural = "Ресурсы"
        default_related_name = "resources"
        default_related_name = "resources"

    def __str__(self):
        return f"{self.title}"