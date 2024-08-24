from django.db import models


class CPU(models.Model):
    name = models.CharField(max_length=100)
    socket = models.CharField(max_length=100)
    cores = models.IntegerField()
    thread = models.IntegerField()
    power = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class GPU(models.Model):
    name = models.CharField(max_length=100)
    socket = models.CharField(max_length=100)
    cores = models.IntegerField()
    thread = models.IntegerField()
    power = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class Motherboard(models.Model):
    name = models.CharField(max_length=100)
    socket = models.CharField(max_length=100)
    chipset = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class RAM(models.Model):
    name = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class StorageDrive(models.Model):
    name = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class PowerSupply(models.Model):
    name = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class CoolingSystem(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class Case(models.Model):
    name = models.CharField(max_length=100)
    proportions = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    company = models.CharField(max_length=100)


class AssemblerPC(models.Model):
    name = models.CharField(max_length=100)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    storage_drive = models.ForeignKey(StorageDrive, on_delete=models.CASCADE)
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE)
    cooling_system = models.ForeignKey(CoolingSystem, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    price_all = models.DecimalField(decimal_places=2, max_digits=6)
    user_score = models.DecimalField(decimal_places=2, max_digits=6)