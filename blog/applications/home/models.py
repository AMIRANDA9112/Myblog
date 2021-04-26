from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono Contacto',
        max_length=20
    )

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural= 'Suscriptores'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):

    full_name = models.CharField(
        'Nombres',
        max_length=60
    )

    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'mensaje'
        verbose_name_plural= 'mensajes'

    def __str__(self):
        return self.full_name



