from django.db import models

# Create your models here.
class Cuenta(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    nacionalidad = models.CharField(max_length=30, null=True, blank=True)
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField()
    fecha_de_alta = models.DateField()
    domicilio = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
        
    def __str__(self):
        return self.apellido
        #return "Apellido y Nombre: " + self.apellido,self.nombre + " - D.N.I.: " + str(self.dni)
        
