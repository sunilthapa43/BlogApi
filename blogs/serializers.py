from rest_framework import serializers
from  django.contrib.auth import get_user_model #new
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        #if you want everything sorted in your own order please make it like   fields = ('first' ,'second', 'third')



class UserSerializer(serializers.ModelSerializer):
    class Meta: 

        model =get_user_model()
        fields = ('id', 'username')


#now lets see viewsets and routers