from django import forms
from . import models

class TweetForm(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = ["content"]