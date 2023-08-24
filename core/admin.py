from django.contrib import admin
from core.models import Usuario, Teste

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario)
admin.site.register(Teste)

