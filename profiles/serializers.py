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

    def create(self, validated_data):
        """
        Handle writable nested serializer to create a new profile.
        :param validated_data: validated data, by serializer class's validate method
        :return: updated Profile model instance
        """

        data = validated_data.copy()
        data.pop('images')  # deleting 'images' list as it is not going to be used

        '''
        Fetching `images` list of image files explicitly from context.
        Because using default way, value of `images` received at serializers from viewset was an empty list.
        However value of `images` in viewset were OK.
        Hence applied this workaround.   
        '''
        images_data = self.context.get('request').data.pop('images')
        try:
            profile = Profile.objects.create(**data)
        except TypeError:
            msg = (
                    'Got a `TypeError` when calling `Post.objects.create()`.'
            )
            raise TypeError(msg)
        try:
            for image_data in images_data:

                image, created = Image.objects.get_or_create(image=image_data)
                profile.images.add(image)

            return profile
        except TypeError:
            profile = Profile.objects.get(pk=profile.id)
            profile.delete()
            msg = (
                    'Got a `TypeError` when calling `Image.objects.get_or_create()`.'
            )
            raise TypeError(msg)

        return profile

    def update(self, instance, validated_data):
        """
        Handle writable nested serializer to update the current profile.
        :param instance: current Profile model instance
        :param validated_data: validated data, by serializer class's validate method
        :return: updated Profile model instance
        """

        '''
        overwrite post instance fields with new data if not None, else assign the old value
        '''
        instance.info = validated_data.get('info', instance.content)
        instance.avatar = validated_data.get('avatar', instance.avatar)

        try:

            '''
            Fetching `images` list of image files explicitly from context.
            Because using default way, value of `images` received at serializers from viewset was an empty list.
            However value of `images` in viewset were OK.
            Hence applied this workaround.   
            '''
            images_data = self.context.get('request').data.pop('images')
        except:
            images_data = None

        if images_data is not None:
            image_instance_list = []
            for image_data in images_data:
                image, created = Image.objects.get_or_create(image=image_data)
                image_instance_list.append(image)

            instance.images.set(image_instance_list)

        instance.save()  # why? see base class code; need to save() to make auto_now work
        return instance
