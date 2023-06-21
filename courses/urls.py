from django.urls import path
from . import views

urlpatterns = [
    path('mynotes/', views.upload_notes, name="mynote"),
    path('mycourse/', views.my_course, name="mycourse"),
    path('collection/', views.collection, name="collection"),
    path('public_note/', views.public_notes, name="public_note"),
    path('note/<int:note_id>/', views.note_contents, name='note_content'),
    path('material/', views.material, name="material")
    # path('test/', views.note_content, name='note_content'),
]
