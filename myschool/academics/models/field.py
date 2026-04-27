from django.db import models
from django.utils.translation import gettext_lazy as _


class Field(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Nom")
    )

    description = models.TextField(
        blank=True,
        verbose_name=_("Description")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de creation")
    )

    class Meta:
        verbose_name = "Filière"
        verbose_name_plural = "Filières"

    def __str__(self):
        return self.name