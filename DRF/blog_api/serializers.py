# Serializer allows the data from queryset or models or database 
# to be converted to python datatypes then that can be easily 
# render it to JSON and pass the data to our application.

from rest_framework import serializers
from  blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ( 'id', 'title', 'author', 'excerpt', 'content', 'status')
