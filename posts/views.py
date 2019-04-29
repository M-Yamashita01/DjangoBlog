from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    posts = Post.objects.order_by('-published')
    return render(request, "posts/index.html", {"posts": posts})


# def index(request):
    # posts = Post.objects.order_by('-published')
    # 
    # return render(request, "posts/index.html", {"num": range(10)},)
