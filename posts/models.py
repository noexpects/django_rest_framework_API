from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=120)
    slug = models.SlugField(
        verbose_name="Slug",
        unique=True,
        blank=True,
        default="",
        max_length=250,
        editable=False,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default="0", blank=True, editable=False)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("id",)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", verbose_name="Post", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, related_name="comments", verbose_name="Author", on_delete=models.CASCADE
    )
    content = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("id",)
