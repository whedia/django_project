from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView # new
from django.urls import reverse_lazy # new

from .forms import PostForm # new
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class DeletePostView(DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')
