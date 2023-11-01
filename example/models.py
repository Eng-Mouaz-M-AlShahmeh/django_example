from django.db import models
from django import forms


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class CommentForm(forms.Form):
    author = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
