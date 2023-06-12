from django.db import models

# Create your models here.
class Artista(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=30, null=True, blank=True)
    
    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
        
    def __str__(self):
        return self.apellido
        #return "Apellido y Nombre: " + self.apellido, self.nombre
