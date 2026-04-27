from django.db import models
from django.utils.translation import gettext_lazy as _


class Absence(models.Model):

    student = models.ForeignKey(
        "accounts.Student",
        verbose_name=_("Etudiant"),
        related_name="std_absence",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        "academics.Course",
        verbose_name=_("Cours"),
        related_name="absences",
        on_delete=models.CASCADE,
    )

    date = models.DateField(
        verbose_name=_("Date")
    )

    justified = models.BooleanField(
        default=False,
        verbose_name=_("Justifiée")
    )

    reason = models.TextField(
        blank=True,
        verbose_name=_("Motif")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Créé le")
    )

    class Meta:
        verbose_name = "Absence"
        verbose_name_plural = "Absences"

    def __str__(self):
        return f"{self.student} - {self.course} - {self.date}"