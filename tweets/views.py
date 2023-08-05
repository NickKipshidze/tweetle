from django.shortcuts import render, redirect
from django.views import View
from . import forms, models

# Create your views here.

class ExploreView(View):
    def get(self, request):
        username = None
        
        if request.user.is_authenticated:
            username = request.user.username
                    
        return render(request, "explore.html", {
            "form": forms.TweetForm(),
            "tweets": models.Tweet.objects.all()[::-1],
            "username": username
        })
    
    def post(self, request):
        form = forms.TweetForm(request.POST)
        
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            
            return redirect("explore")