from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

class TestRoute(View):
    def get(self, request):
        return HttpResponse("<h1>Works</h1>")
