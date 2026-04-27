from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _




class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):


    role_choices = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    
    username = None 

    email = models.EmailField(
        unique=True,
        verbose_name=_("Email")
    )

    role = models.CharField(
        max_length=10,
        choices=role_choices,
        verbose_name=_("Rôle")
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Actif")
    )

 
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de création")
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'      
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        # Retourne par exemple : "Nabegna Diabaté (TEACHER)"
        return f"{self.first_name} {self.last_name} ({self.role})"
