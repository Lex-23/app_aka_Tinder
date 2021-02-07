from django.db import models

from users.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like


class Image(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='media')


class Profile(models.Model):
    SEX = (('M', 'Male'), ('F', 'Female'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, null=False, max_length=100)
    gender = models.CharField(max_length=1, choices=SEX, blank=False, default="")
    city = models.CharField(blank=True, null=False, max_length=100)
    info = models.TextField(default=None, blank=True, null=True, verbose_name='add info')
    created = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='media')
    images = models.ManyToManyField(Image, blank=True, related_name='profiles')
    likes = GenericRelation(Like)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile_edit', kwargs={'user': self.user})

    @property
    def total_likes(self):
        return self.likes.count()




