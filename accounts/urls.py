from django.urls import path
from . import views

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("<str:username>", views.ProfileView.as_view(), name="profile")
]
