from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions


from blog.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This set of views automatically creates the `list` and `detail ' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    This set of views automatically provides the actions 'list`, 'create', ' extract`,
    'update` and 'destroy'.
    """
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
