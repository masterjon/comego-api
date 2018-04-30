from django.contrib import admin
from .models import CategoryItem, ActivityCategory, Salon, Actividad, Boletin, Guia, Norma, Reglamento, Ley, Podcast, UrlItem


@admin.register(CategoryItem)
class CategoryItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    pass


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
