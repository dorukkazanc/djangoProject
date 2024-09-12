from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PostViewSet, TodoViewSet, AlbumViewSet, PhotoViewSet, CommentViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('todos', TodoViewSet)
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]