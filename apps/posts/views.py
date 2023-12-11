from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.posts.models import Post
from apps.posts.serializers import PostSerialazer

# Create your views here.
class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer

class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer
