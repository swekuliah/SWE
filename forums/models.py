from django.db import models
from courses.models import materials

# Create your models here.
# Create your models here.
class forum(models.Model):
    parent_materials = models.ForeignKey(
        materials, 
        related_name="parent_materials", 
        on_delete=models.CASCADE
    )
    count = models.IntegerField()

class thread(models.Model):
    parent_forum = models.ForeignKey(
        "forum",
        related_name="parent_forum",
        on_delete=models.CASCADE
    )

class post(models.Model):
    content = models.TextField()
    parent_thread = models.ForeignKey(
        "thread", 
        related_name="parent_thread", 
        on_delete=models.CASCADE
    )

class reply(models.Model):
    replied_to = models.CharField(max_length=255)