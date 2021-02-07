from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['name']

    ordering_fields = ['gender', 'city']
    ordering = ['gender', 'city', 'id']
