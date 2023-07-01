from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eintrag(models.Model):
    author = models.ForeignKey(User, verbose_name=("Verfasser"), on_delete=models.CASCADE)
    ueberschrift = models.CharField("Überschrift", max_length=50)
    slug = models.SlugField("Schlagwort")
    text = models.TextField("Eintrag")
    erstellt = models.DateTimeField("Erstellt", auto_now=False, auto_now_add=True)
    geaendert = models.DateTimeField("Geändert", auto_now=True, auto_now_add=False)
    aktiv = models.BooleanField("Aktiv", default=True)
    class Meta:
        verbose_name = "Eintrag"
        verbose_name_plural = "Einträge"
        ordering = ['-geaendert']

    def __str__(self):
        return f"{self.ueberschrift} / {self.slug} ({self.author})"

    def get_absolute_url(self):
        return reverse("Eintrag_detail", kwargs={"pk": self.pk})
