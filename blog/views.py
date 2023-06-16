from rest_framework import generics
from . serializers import BlogPostSerializer
from . models import BlogPost
from rest_framework_simplejwt import authentication
import datetime

x = datetime.datetime.now()

class BlogPostListCreateView(generics.ListCreateAPIView):
    authentication_classes = [
        authentication.JWTAuthentication,
        ] 
    queryset = BlogPost.objects.all()
    serializer_class =  BlogPostSerializer

    def perform_create(self, serializer):
        date = serializer.validated_data.get('date')
        if date is None:
            date = f'{x.strftime("%c")}'
        serializer.save( date=date)

class BlogPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class =  BlogPostSerializer
    lookup_field = 'pk'


blogView = BlogPostView.as_view()    
blogCreateView = BlogPostListCreateView.as_view()