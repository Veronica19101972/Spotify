from django.db import models

# Create your models here.
class Album(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_de_lanzamiento = models.DateField()
    estilo = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbumes"
        
    def __str__(self):
        return self.nombre
        #return "Nombre: " +self.nombre + "Estilo de Musica: " +self.estilo
    