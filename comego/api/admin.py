from django.contrib import admin
from . import models


@admin.register(models.CategoryItem)
class CategoryItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


class PresentacionTabAdmin(admin.StackedInline):
    model = models.Presentacion


@admin.register(models.Actividad)
class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ('month',)
    list_display = ["title", "category", "start_date", "ordering"]
    list_filter = ["category"]
    inlines = [PresentacionTabAdmin]


@admin.register(models.Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ["title", "actividad"]
    list_filter = ["actividad"]


class UrlItemInline(admin.StackedInline):
    model = models.UrlItem


@admin.register(models.Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_filter = ["category"]
    inlines = [UrlItemInline]


@admin.register(models.Boletin)
class BoletinAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Guia)
class GuiaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Norma)
class NormaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Reglamento)
class ReglamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ley)
class LeyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    pass
