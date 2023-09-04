from django.contrib import admin
from core.models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario)

