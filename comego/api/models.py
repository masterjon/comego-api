# -*- coding: utf-8 -*-
from django.db import models


class Boletin(models.Model):
    title = models.CharField('Título', max_length=50)
    url = models.URLField(blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Boletines'
        ordering = ['-ordering']

    def __str__(self):
        return self.title


class Guia(models.Model):
    title = models.CharField('Título', max_length=200)
    url = models.URLField(blank=True, default='http://tv.comego.org.mx/')
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-ordering']

    def __str__(self):
        return self.title


class Norma(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-ordering']

    def __str__(self):
        return self.title


class Reglamento(models.Model):
    title = models.CharField('Título', max_length=200)
    url = models.URLField(blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-ordering']

    def __str__(self):
        return self.title


class Ley(models.Model):
    title = models.CharField('Título', max_length=200)
    url = models.URLField(blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Leyes'
        ordering = ['-ordering']

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
        ordering = ['-ordering']

    def __str__(self):
        return self.title


class UrlItem(models.Model):
    url = models.URLField()
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
