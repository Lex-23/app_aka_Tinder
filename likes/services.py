from django.contrib.contenttypes.models import ContentType
from .models import Like, Dislike
from users.models import User


def add_like(obj, user):
    """Лайкает `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return like


def remove_like(obj, user):
    """Удаляет лайк с `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def is_fan(obj, user) -> bool:
    """Проверяет, лайкнул ли `user` `obj`."""
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return likes.exists()


def get_fans(obj):
    """Получает всех пользователей, которые лайкнули `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        likes__content_type=obj_type, likes__object_id=obj.id)


def add_dislike(obj, user):
    """дизайкает `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    dislike, is_created = Dislike.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return dislike


def remove_dislike(obj, user):
    """Удаляет дизлайк с `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    Dislike.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def is_unfan(obj, user) -> bool:
    """Проверяет, дизлайкнул ли `user` `obj`."""
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    dislikes = Dislike.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return dislikes.exists()


def get_unfans(obj):
    """Получает всех пользователей, которые дизлайкнули `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        dislikes__content_type=obj_type, dislikes__object_id=obj.id)
