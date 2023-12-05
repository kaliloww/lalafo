from rest_framework.generics import ListAPIView

from apps.posts.models import Post
from apps.posts.serializers import PostSerialazer

# Create your views here.
class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer