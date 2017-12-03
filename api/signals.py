from django.conf import settings
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm

from .models import UserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='create_new_user_profile')
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a Profile instance for all newly created User instances. We only
    run on user creation to avoid having to check for existence on each call
    to User.save.
    """
    user = instance
    if created and user.email != settings.ANONYMOUS_USER_NAME:
        profile = UserProfile.objects.create(user=user)
        assign_perm('api.view_userprofile', user, profile)
        assign_perm('api.change_userprofile', user, profile)
        can_view_profile = Permission.objects.get(codename='view_userprofile')
        user.user_permissions.add(can_view_profile)
