from django.urls import path, include
from rest_framework_nested import routers

from .views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r"posts", PostViewSet)

posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
posts_router.register(r"comments", CommentViewSet, basename="comment")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]
