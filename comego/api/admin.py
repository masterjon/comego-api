from django.contrib import admin
from .models import Boletin, Guia, Norma, Reglamento, Ley


# Register your models here.
@admin.register(Boletin)
class BoletinAdmin(admin.ModelAdmin):
    pass


@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    pass


@admin.register(Norma)
class NormaAdmin(admin.ModelAdmin):
    pass


@admin.register(Reglamento)
class ReglamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Ley)
class LeyAdmin(admin.ModelAdmin):
    pass
