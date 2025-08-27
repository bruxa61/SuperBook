from django.shortcuts import render
from django.views.generic import ListView
from .models import Hero


#FBV - function-based view - view baseada em função
def lista_herois(request):
    herois = Hero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"herois": herois})

#CBV - CLASS-BASED VIEW - VIEW BASEADA EM CLASSE COM GENERIC LIST VIEW
class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"