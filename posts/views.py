from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.views.generic import ListView, CreateView # new
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

def delete(request, pk, template_name='posts/confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request, template_name, {'object':post})