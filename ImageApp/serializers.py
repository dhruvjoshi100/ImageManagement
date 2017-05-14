from rest_framework import serializers
from ImageApp.models import MyPhoto
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    #image = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'image',)

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = MyPhoto
        fields = ('url', 'id', 'image', 'owner')
        owner = serializers.Field(source='owner.username')



