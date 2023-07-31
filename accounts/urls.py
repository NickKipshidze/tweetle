from django.urls import path
from . import views

urlpatterns = [
    path("test", views.TestRoute.as_view(), name="test")
]
