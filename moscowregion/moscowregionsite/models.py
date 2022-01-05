from django.db import models, connection
from django.utils.translation import gettext_lazy as _


class Locality(models.Model):
    class LocalitySubordination(models.TextChoices):
        REGIONAL = 'RE', _('Областное подчинение')
        DISTRICT = 'DI', _('Районное подчинение')
        CLOSED = 'CL', _('ЗАТО')

    subordination = models.CharField(
        max_length=2,
        choices=LocalitySubordination.choices,
        default=LocalitySubordination.DISTRICT,
        verbose_name="Подчинение"
    )
    name = models.CharField(max_length=100, verbose_name="Название", unique=True)
    url = models.URLField(max_length=255, verbose_name="Ссылка")
    unit = models.CharField(max_length=100, verbose_name="Административная единица")
    OKATO = models.CharField(max_length=50, verbose_name="ОКАТО")
    population = models.IntegerField(verbose_name="Население")
    founded = models.CharField(default=None, blank=True, null=True, max_length=20, verbose_name="Основан")
    city_status = models.CharField(default=None, blank=True, null=True, max_length=20, verbose_name="Статус города")
    category = models.CharField(blank=True, max_length=50, verbose_name="Категория")

