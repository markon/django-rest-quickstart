from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name',)
        read_only_fields = ('username', )


class UserProfileSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:userprofile-detail")

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
