from django.db import models
from django.utils.translation import gettext_lazy as _


class Enrollment(models.Model):

    class Status(models.TextChoices):
        active    = 'active',    'Actif'
        completed = 'completed', 'Terminé'
        dropped   = 'dropped',   'Abandonné'

    student = models.ForeignKey(
        "accounts.Student",
        verbose_name=_("Etudiant"),
        related_name="enrollments",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        "academics.Course",
        verbose_name=_("Cours"),
        related_name="enrollments",
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.active,
        verbose_name=_("Statut")
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Inscrit le")
    )

    class Meta:
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"
        unique_together = ['student', 'course']

    def __str__(self):
        return f"{self.student} - {self.course}"