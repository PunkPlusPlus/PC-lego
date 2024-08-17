from django.db import models

class Processors(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return (f'Name: {self.name}, Description: {self.description}')


class Motherboards(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class RAM(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class VideoCards(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class HDD(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class SSD(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class PowerSupplies(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class Case(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class Monitors(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class Keyboards(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class Mouse(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')


class Headphones(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')

