from django.db import models

class Persona(models.Model):
    """Model definition for Persona."""

    nombre = models.CharField(verbose_name="nombre completo", max_length=50)
    edad = models.IntegerField(verbose_name="edad")
    email = models.EmailField(verbose_name="correo electrónico", max_length=254)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        return f"{self.nombre} - {self.email}"

