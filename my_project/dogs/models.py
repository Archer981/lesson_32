from django.db import models

class Dog(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя собачки",
        help_text="Укажите имя собачки"
    )
    breed = models.CharField(
        max_length=50,
        verbose_name="Порода собачки",
        help_text="Укажите породу собачки"
    )

    class Meta:
        verbose_name_plural = "Собачки"
        verbose_name = "Собачка"