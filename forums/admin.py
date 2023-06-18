from django.contrib import admin
from .models import forum, thread, post, reply

# Register your models here.
admin.site.register(forum)
admin.site.register(thread)
admin.site.register(post)
admin.site.register(reply)