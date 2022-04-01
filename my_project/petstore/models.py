from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Заявка"
        verbose_name = "Заявки"
