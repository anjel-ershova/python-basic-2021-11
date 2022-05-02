from django.contrib.auth.models import User, AbstractUser
from django.db import models


# расширение дефолтного User
# class NewUserProfile(models.Model):
#     user = models.OneToOneField(User,
#                                 on_delete=models.CASCADE,
#                                 primary_key=True)
#     avatar = models.ImageField(upload_to='avatars', blank=True)

class CharlistUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)
