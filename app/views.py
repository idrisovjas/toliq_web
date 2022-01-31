from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import DetailView,UpdateView
from django.views.generic.edit import CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class BlogView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','text']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_edit.html'
    fields = ['title','text']
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
