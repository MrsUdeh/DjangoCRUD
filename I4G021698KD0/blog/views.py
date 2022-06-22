from django.shortcuts import render

from I4G021698KD0.blog.models import Post
from django.views.generic.edit import CreateView
from .models import Post
# Create your views here.
class PostCreateView(CreateView):
    model = Post