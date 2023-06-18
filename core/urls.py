from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('', RedirectView.as_view(url='register/')),
    path('profile/', views.profile, name="profile"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_user, name="logout"),
]
