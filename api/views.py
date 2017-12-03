from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
