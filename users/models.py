from django.db import models

class Users(models.Model):
    username = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта', max_length=20)
    password = models.TextField('Пароль', max_length=20)

    def __str__(self):
        return (f'Name: {self.name}')
