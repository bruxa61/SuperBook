from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


#FBV - function-based view - view baseada em função
def lista_posts(request):
    posts = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})

#CBV - CLASS-BASED VIEW - VIEW BASEADA EM CLASSE COM GENERIC LIST VIEW
class HeroListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"