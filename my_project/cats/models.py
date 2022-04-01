from django.db import models


class Cat(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя котика",
        help_text="Укажите имя котика"
    )
    breed = models.CharField(
        max_length=50,
        verbose_name="Порода котика",
        help_text="Укажите породу котика"
    )

    class Meta:
        verbose_name_plural = "Котики"
        verbose_name = "Котик"
