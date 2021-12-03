import time
import typing

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Post


@receiver(post_save, sender=Post)
def generate_slug_from_title(instance: Post, **kwargs: typing.Any) -> None:
    if not instance.slug:
        instance.slug = slugify(instance.title)
        if Post.objects.filter(slug=instance.slug).exists():
            instance.slug += f"-{time.time()}"
        instance.save()
