from django.db import models

# Create your models here.
class Corredor(models.Model):
    SEX_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    )
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    sexo = models.CharField(max_length=2, choices=SEX_CHOICES)
    lorigen = models.CharField(max_length=50)
    lresidencia = models.CharField(max_length=50)
    correoElectronico = models.EmailField(max_length=60)
    direccion = models.CharField(max_length=70)
    codigoPostal = models.IntegerField(max_length=5)
    estado = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=25)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    equipo = models.CharField(max_length=70)

    def nombre_completo(self):
        nombreCompleto = '%s %s %s' % (
            self.nombre, self.apellidoPaterno, self.apellidoMaterno)
        return nombreCompleto

    def imagen_nombre(self):
        nombre = '%s-%s' % (self.apellidoPaterno, self.nombre)
        return nombre

    def __unicode__(self):
        return self.nombre_completo()