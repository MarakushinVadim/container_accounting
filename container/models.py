from django.db import models
from client.models import Client

NULLABLE = {"blank": True, "null": True}

class Container(models.Model):
    number = models.CharField(max_length=20, verbose_name='Номер баллона')
    manufacture_year = models.DateField(**NULLABLE, verbose_name='Год производства')
    status_hydrotesting = models.BooleanField(verbose_name='Гидроиспытание')
    volume = models.PositiveIntegerField(verbose_name='Обьем быллона')
    client = models.ForeignKey(Client, verbose_name='Владелец', on_delete=models.CASCADE)
    on_refueling = models.BooleanField(verbose_name='На заправке', default=False)

    class Meta:
        verbose_name = "Баллон"
        verbose_name_plural = "Баллоны"

    def __str__(self):
        return f'Баллон номер - {self.number} Владелец - {self.client.name}'
