from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.settings import api_settings
from .models import Profile
from .serializers import ProfileSerializer


from rest_framework.response import Response


# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    """
    Profile ModelViewSet.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
