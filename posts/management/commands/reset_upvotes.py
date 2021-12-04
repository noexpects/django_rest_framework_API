from django.core.management.base import BaseCommand

from posts.models import Post


class Command(BaseCommand):
    help = 'Resets all posts upvotes'

    def handle(self, *args, **options) -> None:
        Post.objects.all().update(upvotes=0)
