"""Post views."""

# Django Rest Framework
from rest_framework import viewsets

# Own
from render_test_01.api.serializers import PostModelSerializer
from render_test_01.api.models import Post

class PostViewSet(viewsets.ModelViewSet):
    """ Post view set
        Handle all CRUD requests
    """

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    
       