from django.db import models
from django.utils.translation import gettext_lazy as _


class Level(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name=_("Nom")
    )

    field = models.ForeignKey(
        "academics.Field",
        verbose_name=_("Filière"),
        related_name="levels",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Créé le")
    )

    class Meta:
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"

    def __str__(self):
        return f"{self.name} - {self.field}"