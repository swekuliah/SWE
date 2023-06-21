from django.db import models
from django.contrib.auth.models import User

# Create your models here
# one on one mode with default user to, i created this to add profile picture to default django user.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields if user want to upload profile picture
    profile_pic = models.FileField(upload_to="./static/user_profile", default=None)
    # jujur aja ku lupa kenapa tk bikin ini :v
    location = models.CharField(max_length=255, blank=True)