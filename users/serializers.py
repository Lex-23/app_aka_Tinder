from rest_framework import serializers

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    # Field for second enter password
    password2 = serializers.CharField()

    class Meta:
        model = User
        field = ['username', 'email', 'password', 'password2']

    # methods for saving new user
    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        # checking for validate password
        password = self.validated_data['password']
        # checking for validate password2
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: "Password don't exist"})

        # saving password
        user.set_password(password)
        user.save()
        return user
