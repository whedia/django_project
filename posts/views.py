from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy 
from .forms import PostForm 
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home') #retour a page d'acceuil en cas de bon execution de la requete

class DeletePostView(DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home') #retour a page d'acceuil en cas de bon execution de la requete

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit.html'
    success_url = reverse_lazy('home') #retour a page d'acceuil en cas de bon execution de la requete

    