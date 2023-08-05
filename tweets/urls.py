from django.urls import path
from . import views

urlpatterns = [
    path("explore", views.ExploreView.as_view(), name="explore")
]
