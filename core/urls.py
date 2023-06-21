from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('', RedirectView.as_view(url='register/')),
    path('profile/', views.profile, name="profile"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/edit/', views.edit_profile_page, name="edit_profile"),
    path('profile/edit/commit', views.edit_profile, name="commit_edit"),
    path('profile/edit/commit-pic', views.edit_profile_pic, name="commit_pic_edit"),
    path('logout/', views.logout_user, name="logout"),
]
