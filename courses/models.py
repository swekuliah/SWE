from django.db import models
from django.utils import timezone
# from core.models import UserProfile ku lupa buat apa ni, keknya penting diemin jak
from django.contrib.auth.models import User

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    # ini nanti kasi trigger kalo bisa
    follower = models.IntegerField()
    

class followed_course(models.Model):
    # parent_materials = models.ForeignKey(
    #     user, 
    #     on_delete=models.CASCADE
    # )
    count = models.IntegerField()


class materials(models.Model):
    material_title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=255)
    # parent_course = models.ForeignKey(
    #         course,
    #         on_delete=models.CASCADE
    # )


class notes(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120, null=True)
    description = models.TextField(max_length=255)
    note_file = models.FileField(upload_to="./static/upload_notes/", default=None)
    created_on = models.DateField(default=timezone.now)
    is_private = models.BooleanField(null=True)

    # parent_materials = models.ForeignKey(
    #     materials, 
    #     on_delete=models.CASCADE
    # )
    # author = models.ForeignKey(
    #     User,
    #     # null=True,
    #     on_delete=models.CASCADE
    # )
    # def __str__(self):
    #     return "%s" %(self.title)

