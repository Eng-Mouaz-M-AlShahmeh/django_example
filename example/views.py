# from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def say_hi(request):
    # Pull data from db
    # Transform
    # Send email
    # return HttpResponse("Hello, World!")
    posts = Post.objects.all()
    return render(request, "hi.html", {"name": "Eng Mouaz M. Al-Shahmeh", "posts": posts})
