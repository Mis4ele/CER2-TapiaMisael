from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIPO_CHOICES = [
    ('S', 'Suspensión de actividades'),
    ('C', 'Suspensión de clase'),
    ('I', 'Información')
]

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='webComunicados/static/webComunicados/img/logosEntidad/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    detalle = models.CharField(max_length=500)
    detalle_corto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='S')
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateField()
    fecha_modificacion = models.DateField()
    publicado_por = User
    modificado_por = User

    def __str__(self):
        return self.titulo