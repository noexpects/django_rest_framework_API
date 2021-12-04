from django.core.management.base import BaseCommand

from posts.models import Post


class Command(BaseCommand):
    help = 'Resets all posts upvotes'

    def handle(self, *args, **options):
        posts = Post.objects.all()
        for post in posts:
            post.upvotes = 0
            post.save()
