# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class CategoryItem(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)
    link = models.URLField(blank=True, max_length=500)

    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['ordering']

    def __str__(self):
        return self.title


class ActivityCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryItem, related_name='activity_category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categorias de Actividades'

    def __str__(self):
        return self.title


class Salon(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Salones'

    def __str__(self):
        return self.title


class Actividad(models.Model):
    dress_options = (
        ('formal', 'Formal',),
        ('casual', 'Casual',)
    )
    category = models.ForeignKey(ActivityCategory, related_name='actividades', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = RichTextField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    dress_code = models.CharField('Código de vestir', choices=dress_options, max_length=50)
    academic_program_url = models.URLField('Url Programa Académico', blank=True, max_length=500)
    inscription_url = models.URLField('Url Inscripción', blank=True, max_length=500)
    ordering = models.PositiveSmallIntegerField(default=0)
    month = models.CharField(max_length=50, null=False, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Actividades'
        ordering = ['start_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.month = self.start_date.strftime("%B")
        super(Actividad, self).save(*args, **kwargs)


class Boletin(models.Model):
    title = models.CharField('Título', max_length=50)
    url = models.URLField(blank=True, max_length=500)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Boletines'
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Guia(models.Model):
    title = models.CharField('Título', max_length=200)
    url = models.URLField(blank=True, default='http://tv.comego.org.mx/', max_length=500)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Norma(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, max_length=500)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Reglamento(models.Model):
    title = models.CharField('Título', max_length=200)
    url = models.URLField(blank=True, max_length=500)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Ley(models.Model):
    title = models.CharField('Título', max_length=200)
    url = models.URLField(blank=True, max_length=500)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Leyes'
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Podcast(models.Model):
    category_options = (
        ('y_tu_como_lo_haces', 'Y tú como lo haces',),
        ('informativo', 'Informativo',),
    )
    title = models.CharField('Título', max_length=200)
    category = models.CharField(choices=category_options, max_length=50)
    picture = models.ImageField(null=True, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class UrlItem(models.Model):
    title = models.CharField('Título', max_length=50)
    url = models.URLField(max_length=500)
    podcast = models.ForeignKey(Podcast, related_name='parts', on_delete=models.CASCADE)


class Sponsor(models.Model):
    title = models.CharField('Título', max_length=50)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=500)
    picture = models.ImageField(null=True, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Anuncio(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(help_text="694 × 124")
    link = models.URLField(max_length=500, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

