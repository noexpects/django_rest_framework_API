from django.db.models import QuerySet
from django.db.models import F
from django.http import HttpRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=["post"])
    def upvote(self, request: HttpRequest, pk: int = None) -> Response:
        Post.objects.filter(pk=pk).update(upvotes=F('upvotes')+1)
        return Response({"status": "post upvoted"})


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self) -> "QuerySet[Comment]":
        return Comment.objects.filter(post_id=self.kwargs["post_pk"])
