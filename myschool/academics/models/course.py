from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name=_("Nom")
    )

    description = models.TextField(
        blank=True,
        verbose_name=_("Description")
    )

    teacher = models.ForeignKey(
        "accounts.Teacher",
        verbose_name=_("Enseignant"),
        related_name="courses",
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de création")
    )

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.name