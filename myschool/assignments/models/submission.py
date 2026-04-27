from django.db import models
from django.utils.translation import gettext_lazy as _


class Submission(models.Model):

    assignment = models.ForeignKey(
        "assignments.Assignment",
        verbose_name=_("Devoir"),
        related_name="submissions",
        on_delete=models.CASCADE,
    )

    student = models.ForeignKey(
        "accounts.Student",
        verbose_name=_("Etudiant"),
        related_name="std_submissions",
        on_delete=models.CASCADE,
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Déposé le")
    )

    class Meta:
        verbose_name = "Soumission"
        verbose_name_plural = "Soumissions"

    def __str__(self):
        return f"{self.student} - {self.assignment}"