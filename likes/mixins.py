from rest_framework.decorators import action
from rest_framework.response import Response
from . import services
from .serializers import FanSerializer, UnFanSerializer


class LikedMixin:
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """Лайкает `obj`.
        """
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """Удаляет лайк с `obj`.
        """
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`.
        """
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)


class DislikedMixin:
    @action(detail=True, methods=['POST'])
    def dislike(self, request, pk=None):
        """Дизлайкает `obj`.
        """
        obj = self.get_object()
        services.add_dislike(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def undislike(self, request, pk=None):
        """Удаляет дизлайк с `obj`.
        """
        obj = self.get_object()
        services.remove_dislike(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def unfans(self, request, pk=None):
        """Получает всех пользователей, которые дизлайкнули `obj`.
        """
        obj = self.get_object()
        unfans = services.get_unfans(obj)
        serializer = UnFanSerializer(unfans, many=True)
        return Response(serializer.data)
