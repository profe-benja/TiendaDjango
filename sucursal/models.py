from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    clave = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.nombre} {self.correo}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=256)
    codigo = models.CharField(max_length=100, unique=True)
    precio = models.IntegerField()
    foto = models.FileField(upload_to="uploads/", null=True, blank=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ${self.precio}"

    
    