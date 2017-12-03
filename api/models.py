import uuid

from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    """This model stores all information relative to a user which doesn't belong to
    authentication."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        permissions = (
            ('view_userprofile', 'View UserProfile'),
        )

    def __str__(self):
        return self.user.username
