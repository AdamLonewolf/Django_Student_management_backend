from django.db import models
from django.utils.translation import gettext_lazy as _


class Assignment(models.Model):


    course = models.ForeignKey(
    'academics.Course',
    on_delete=models.CASCADE,
    related_name='assignments',
    verbose_name=_("Cours")
    )

    title = models.CharField(
        verbose_name=_("Titre"),
        max_length=50
    )

    description = models.TextField(
        verbose_name=_("Description"),
        max_length=3000
    )

    due_date = models.DateField(
    verbose_name=_("Date limite")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de création")
    )

    class Meta:
        verbose_name = "Devoir"
        verbose_name_plural = "Devoirs"

    def __str__(self):
        return f"{self.title} - {self.course}"