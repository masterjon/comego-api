from django.contrib import admin
from .models import Boletin, Guia, Norma, Reglamento, Ley, Podcast, UrlItem


class UrlItemInline(admin.StackedInline):
    model = UrlItem


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    inlines = [UrlItemInline]


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
