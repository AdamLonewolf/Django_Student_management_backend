from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.profile import Profile

class Parent(Profile):

    class ParentType(models.TextChoices):
        father  = 'father',  'père'
        mother  = 'mother',  'mère'
        guardian = 'guardian', 'tuteur/tutrice'


    parent_type = models.CharField(
        max_length=10,
        choices=ParentType.choices,
        verbose_name="Type"
    )

    students = models.ManyToManyField(
        'accounts.Student',
        related_name='parents',
        blank=True
    )


    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"