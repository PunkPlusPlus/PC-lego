from django.db import models

class TypePC(models.Model):
    type = models.CharField(max_length=100, verbose_name="Тип ПК", help_text="Тип ПК (игровой, офисный)")

    def __str__(self):
        return f'{self.type}'


class CPU(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название процессора")
    socket = models.CharField(max_length=100, verbose_name="Тип сокета")
    cores = models.IntegerField(verbose_name="Количество ядер")
    power = models.CharField(max_length=100, verbose_name="Энергопотребление")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class GPU(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название видиокарты")
    volume = models.CharField(max_length=100, verbose_name="Объем памяти")
    power = models.CharField(max_length=100, verbose_name="Энергопотребление")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class Motherboard(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название материнской платы")
    socket = models.CharField(max_length=100, verbose_name="Тип сокета")
    chipset = models.CharField(max_length=100, verbose_name="Тип чипсета")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class RAM(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название оперативной памяти")
    volume = models.CharField(max_length=100, verbose_name="Объем памяти")
    type = models.CharField(max_length=100, verbose_name="Тип памяти")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class StorageDrive(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название накопителя")
    volume = models.CharField(max_length=100, verbose_name="Объем памяти")
    type = models.CharField(max_length=100, verbose_name="Тип накопителя")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class PowerSupply(models.Model):
    name = models.CharField(max_length=100, verbose_name="Блока питания")
    power = models.CharField(max_length=100, verbose_name="Энергопотребление")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class CoolingSystem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название системы охлаждения")
    destination = models.CharField(max_length=100, verbose_name="Назначение")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class Case(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название корпуса")
    proportions = models.CharField(max_length=100, verbose_name="Габариты")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    company = models.CharField(max_length=100, verbose_name="Производитель")

    def __str__(self):
        return f'{self.name} ({self.company})'


class AssemblerPC(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название сборки", unique = True)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    storage_drive = models.ForeignKey(StorageDrive, on_delete=models.CASCADE)
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE)
    cooling_system = models.ForeignKey(CoolingSystem, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    type_pc = models.ForeignKey(TypePC, on_delete=models.CASCADE)
    price_all = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена за сборку")
    user_score = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Рейтинг")