from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill, ResizeCanvas

# Create your models here.
class User(AbstractUser):
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower')
    # user_set => follower
    image = ProcessedImageField(
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 60},
                                default='default.png',
                                )