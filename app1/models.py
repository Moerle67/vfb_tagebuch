import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Eintrag(models.Model):
    author = models.ForeignKey(User, verbose_name=("Verfasser"), on_delete=models.CASCADE)
    ueberschrift = models.CharField("Überschrift", max_length=50)
    slug = models.SlugField("Schlagwort", unique=True, blank=True)
    text = models.TextField("Eintrag")
    erstellt = models.DateTimeField("Erstellt", auto_now=False, auto_now_add=True)
    geaendert = models.DateTimeField("Geändert", auto_now=True, auto_now_add=False)
    aktiv = models.BooleanField("Aktiv", default=True)
    class Meta:
        verbose_name = "Eintrag"
        verbose_name_plural = "Einträge"
        ordering = ['-geaendert']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ueberschrift)+rand_slug()
        super(Eintrag, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.ueberschrift} / {self.slug} ({self.author})"

    def get_absolute_url(self):
        return reverse("Eintrag_detail", kwargs={"pk": self.pk})

class Kommentar(models.Model):
    eintrag = models.ForeignKey(Eintrag, verbose_name="Blog-Eintrag", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Verfasser", on_delete=models.CASCADE)
    bewertung = models.IntegerField("Bewertung")
    slug = models.SlugField("Schlagwort")
    kommentar = models.TextField("Kommentar")
    erstellt = models.DateTimeField("Erstellt", auto_now=False, auto_now_add=True)
    geaendert = models.DateTimeField("Geändert", auto_now=True, auto_now_add=False)
    aktiv = models.BooleanField("Aktiv", default=True)
    class Meta:
        verbose_name = "Kommentar"
        verbose_name_plural = "Kommentare"
        ordering = ['user', '-geaendert']

    def __str__(self):
        return f"{self.user} - {self.geaendert} / {self.slug}"

    def get_absolute_url(self):
        return reverse("Kommentar_detail", kwargs={"pk": self.pk})
