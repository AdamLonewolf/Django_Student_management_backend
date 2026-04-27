from django.db import models
from django.utils.translation import gettext_lazy as _


class Mark(models.Model):

    enrollment = models.ForeignKey(
        "academics.Enrollment",
        verbose_name=_("Inscription"),
        related_name="marks",
        on_delete=models.CASCADE,
    )

    mark = models.FloatField(
        verbose_name=_("Note")
    )

    remark = models.TextField(
        blank=True,
        verbose_name=_("Observations")
    )

    graded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Noté le")
    )

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"{self.enrollment} - {self.mark}"