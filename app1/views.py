from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib.auth.decorators import permission_required
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

def kommentar_details(request, kommentar_slug):
    ds = get_object_or_404(Kommentar, slug=kommentar_slug, aktiv=True)
    content = {
        'ds': ds,
    }
    return render(request, 'app1/kommentar_detail.html', content)

def form1(request):
    # print(f"Request: '{request.GET}'")
    ausgabe = ""
    fehler = False        
    auswahlg = ("männlich", "weiblich", "divers", "sag ich nicht")
    if 'vname' in request.POST:
        # Rekursiver Aufruf

        vorname = request.POST['vname']
        nachname = request.POST['nname']
        geschlecht  = request.POST['geschlecht']
        if vorname == "":
            ausgabe += "Vorname darf nicht leer sein! "
            fehler = True
        if nachname == "":
            ausgabe += "Nachname darf nicht leer sein! "
            fehler = True
        if not fehler:
            # Kein Fehler
            if geschlecht == "männlich":
                lieb = "lieber"
            elif geschlecht == "weiblich":
                lieb = "liebe"
            elif geschlecht == "divers":
                lieb = ""
            else:
                lieb = "liebe(r)"
            ausgabe = f"Guten Morgen, {lieb} {vorname} {nachname}."
    else:
        # URL Aufruf
        ausgabe = "Das ist der URL-Aufruf"
        vorname = nachname = ""
    content = {
        'ausgabe': ausgabe,
        'auswahlg': auswahlg,
        'vname': vorname,
        'nname': nachname,
    }
    print(ausgabe)
    return render(request, 'app1/formular1.html', content)

@permission_required('app1.view_bild')
def bilder(request):
    bilderliste = Bild.objects.filter()
    print(bilderliste)
    content = {
        'bilderliste': bilderliste,
    }
    return render(request, 'app1/bilder.html', content)