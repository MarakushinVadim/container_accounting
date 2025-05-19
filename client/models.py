from django.db import models

NULLABLE = {"blank": True, "null": True}

class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя клиента')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Клиент {self.name}, с номером телефона {self.phone}'
