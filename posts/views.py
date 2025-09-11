from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy

# def lista_post(request):
#     posts = Post.objects.all()  # busca todos os heróis do banco
#     return render(request, "posts/lista_posts.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('listar_posts')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')