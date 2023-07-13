from django.contrib import admin
from .models import *

class EintragAdmin(admin.ModelAdmin):
  list_display = ("ueberschrift", "text", "author", "slug")
#  prepopulated_fields = {"slug": ("ueberschrift", "author")}

# Register your models here.
admin.site.register(Eintrag, EintragAdmin)
admin.site.register(Kommentar)


  
# admin.site.register(Member, MemberAdmin)