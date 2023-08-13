from django.contrib import admin
from core.models import Usuario,Nome

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario)
admin.site.register(Nome)
