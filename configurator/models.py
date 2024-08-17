from django.db import models
from configurator.interfaces import ComponentTypes
from configurator.exceptions import NotEnoughComponents


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=100, choices=ComponentTypes.choices())


class Assembly(models.Model):
    name = models.CharField(max_length=100)
    components = models.ManyToManyField(Component)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user_score = models.DecimalField(max_digits=5, decimal_places=2)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        for component_type in ComponentTypes:
            component = Assembly.components.get(type=component_type)
            if component is None:
                raise NotEnoughComponents(f"can`t find {component_type}")
        super().save(self, force_insert, force_update, using, update_fields)


