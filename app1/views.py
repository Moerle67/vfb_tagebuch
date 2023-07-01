from django.shortcuts import render
from .models import *

# Create your views here.

def hello(request):
    inhalt = Eintrag.objects.filter(aktiv=True)
    content = {
        'inhalt': inhalt,
        'ueber': "Noch eine neue Überschrift"
    }
    return render(request, 'app1/liste_eintraege.html', content)