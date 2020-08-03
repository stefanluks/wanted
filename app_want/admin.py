from django.contrib import admin
from .models import wanted, bando, texto, usuario

admin.site.register(wanted)
admin.site.register(bando)
admin.site.register(texto)
admin.site.register(usuario)