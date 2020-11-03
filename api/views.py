from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions


from blog.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Этот набор представлений автоматически создает действия `list` и `detail`.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Этот набор представлений автоматически предоставляет действия "список`, `создать`, `извлечь`,
    `обновить` и "уничтожить".
    """
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
