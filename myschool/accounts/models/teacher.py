from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.profile import Profile

class Teacher(Profile):
    
    
    class Gender(models.TextChoices):
        male = 'M', 'Masculin'
        female = 'F', 'Féminin'


    speciality = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Spécialité")
    )


    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        verbose_name=_("Genre")
    )


    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"