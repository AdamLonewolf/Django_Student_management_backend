from django.db import models
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):

    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='%(class)s',
        verbose_name="Utilisateur"
    )

    phone_number = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Téléphone"
    )

    address = models.TextField(
        blank=True,
        verbose_name="Adresse"
    )

    image = models.ImageField(
        upload_to='profiles/',  
        blank=True,
        null=True,
        verbose_name="Photo"
    )

   
    class Meta:
        abstract = True 