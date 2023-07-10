from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.

def hello(request):
    inhalt = Eintrag.objects.filter(aktiv=True)
    content = {
        'inhalt': inhalt,
        'ueber': "Noch eine neue Überschrift"
    }
    return render(request, 'app1/liste_eintraege.html', content)

def eintrag_details(request, eintrag_slug):
    ds = get_object_or_404(Eintrag, slug=eintrag_slug)
    kommentare = Kommentar.objects.filter(eintrag=ds, aktiv=True)
    content = {
        'ds': ds,
        'kommentare': kommentare
    }
    return render(request, 'app1/eintrag_detail.html', content)

def eintrag_neu(request):
    return render(request, 'app1/eintrag_neu.html')

def kommentar_details(request, kommentar_slug):
    ds = get_object_or_404(Kommentar, slug=kommentar_slug, aktiv=True)
    content = {
        'ds': ds,
    }
    return render(request, 'app1/kommentar_detail.html', content)