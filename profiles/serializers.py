from rest_framework import serializers
from .models import Profile, Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id',
                  'name',
                  'user',
                  'gender',
                  'city',
                  'info',
                  'created',
                  'avatar',
                  'user',
                  'images',
                  'url')
