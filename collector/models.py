from django.db import models


class PC(models.Model):
    processor = models.CharField('Наименование', max_length=50)
    motherboard = models.CharField('Наименование', max_length=50)
    ram = models.CharField('Наименование', max_length=50)
    video_card = models.CharField('Наименование', max_length=50)
    hdd = models.CharField('Наименование', max_length=50)
    sdd = models.CharField('Наименование', max_length=50)
    power_supplie = models.CharField('Наименование', max_length=50)
    case = models.CharField('Наименование', max_length=50)
    monitor = models.CharField('Наименование', max_length=50)
    keyboard = models.CharField('Наименование', max_length=50)
    mouse = models.CharField('Наименование', max_length=50)
    headphones = models.CharField('Наименование', max_length=50)


    def __str__(self):
        pass


