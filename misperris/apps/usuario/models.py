from django.db import models

# Create your models here.

#Modelo tipo de vivienda
class TipoVivienda(models.Model):
    nombre = models.CharField(max_length=50)

    def __srt__(self):
        return '{}'.format(self.nombre)

class Usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    correo = models.EmailField()
    run = models.CharField(max_length = 10)
    fecha_nac = models.DateTimeField(default=datetime.now, blank=True)
    telefono = models.CharField(max_length = 14)
    region = models.CharField(max_length = 50)
    comuna = models.CharField(max_length = 50)
    tipo_vivienda = models.ForeignKey(TipoVivienda, default=1, on_delete=models.CASCADE)
    
    def __srt__(self):
        return '{}'.format(self.nombre)