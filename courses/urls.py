from django.urls import path
from . import views

urlpatterns = [
    path('mynotes/', views.upload_notes, name="mynote"),
    path('mycourse/', views.my_course, name="mycourse"),
    path('collection/', views.collection, name="collection"),
    path('note/<int:note_id>/', views.note_contents, name='note_content'),
    # path('test/', views.note_content, name='note_content'),
]