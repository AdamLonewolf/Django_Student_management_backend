from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.profile import Profile

class Student(Profile):


    class Gender(models.TextChoices):
        male = 'M', 'Masculin'
        female = 'F', 'Féminin'

    level = models.ForeignKey(
        "academics.Level", 
        verbose_name=_("Niveau"), 
        on_delete=models.SET_NULL,
        null=True,
        related_name= "students"
    )

    birthdate = models.DateField(
        blank=True,
        null=True, 
        verbose_name=_("Date de naissance")
    )


    student_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Matricule")
    )

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        verbose_name=_("Genre")
    )

    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.student_number}"


