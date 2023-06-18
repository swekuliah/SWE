from django.contrib import admin
from .models import course, followed_course, materials, notes


# Register your models here.
admin.site.register(course)
admin.site.register(followed_course)
admin.site.register(materials)
admin.site.register(notes)