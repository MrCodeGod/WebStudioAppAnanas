from django.db import models


class Content(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class User(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.IntegerField('Возраст', max_length=2)
    email = models.EmailField('E-mail')
    number = models.IntegerField('Номер телефона')