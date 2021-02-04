from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = (
        'username',
        'email',
    )
    search_fields = 'username',
    list_display = (
        'id',
        'username',
        'email',
        'is_active',
        'is_staff',
    )
    list_filter = (
        'is_active',
        'username',
    )


admin.site.register(User, UserAdmin)
