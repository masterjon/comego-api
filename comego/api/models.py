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
    url = models.URLField(blank=True)
    file = models.FileField(blank=True, null=True)
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
