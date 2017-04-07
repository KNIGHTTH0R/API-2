from django.contrib.auth.models import User, Group
from models import Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'first_name','last_name', 'email','is_superuser','date_joined')

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id_post','title','content','tags','author_id','create_time')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')