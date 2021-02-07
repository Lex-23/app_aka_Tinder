from rest_framework import serializers
from .models import Profile, Image
from likes import services as likes_services


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    is_fan = serializers.SerializerMethodField()

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
                  'is_fan',
                  'total_likes',
                  'url')

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` профиль (`obj`)."""
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)
