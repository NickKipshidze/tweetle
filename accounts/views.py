from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.views import View
from . import models
from . import forms

# Create your views here.

class LoginView(View):
    def get(self, request):
        form = forms.LogInForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = forms.LogInForm(request, data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username = form.cleaned_data.get("username"), 
                password = form.cleaned_data.get("password")
            )
            if user is not None:
                auth.login(request, user)
                return redirect(f"/{user}")
        
        return render(request, "login.html", {"form": form})

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect("home")

class SignupView(View):
    def get(self, request):
        form = forms.SignUpForm()
        return render(request, "signup.html", {"form": form})
    
    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
        return render(request, "signup.html", {"form": form})

class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(models.User, username=username)
        username = None
        edit = False
        
        if request.user.is_authenticated and user.username == request.user.username:
            edit = True
        
        if request.user.is_authenticated:
            username = request.user.username
            
        return render(request, "profile.html", {
            "username": username,
            "profile_username": user.username,
            "edit": edit
        })
