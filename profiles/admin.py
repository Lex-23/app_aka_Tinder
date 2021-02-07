from django.contrib import admin

from profiles.models import Profile, Image


class ProfileAdmin(admin.ModelAdmin):
    fields = 'user', 'gender', 'name', 'city', 'info', 'avatar', 'images',
    search_fields = 'user',
    list_display = 'user', 'gender', 'created', 'name', 'city', 'avatar', 'id',
    list_filter = 'city', 'gender',


admin.site.register(Profile, ProfileAdmin)


class ImageAdmin(admin.ModelAdmin):
    fields = 'image',
    list_display = 'image', 'id',


admin.site.register(Image, ImageAdmin)
