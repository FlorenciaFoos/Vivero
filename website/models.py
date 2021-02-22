from django.db import models

# Create your models here.

from django.db import models


class Categoria(models.Model):
    CategoriaId = models.AutoField(primary_key = True, verbose_name = 'ID')
    CategoriaNombre = models.CharField(max_length=200 , verbose_name = 'Nombre de categoría', unique = True)
    CategoriaImagen =  models.ImageField(upload_to ='uploads/',default = 'uploads/None/no-img.jpg,',verbose_name = 'Imagen') 
    def __str__(self):
        """
        String que representa al objeto Categoria
        """
        return self.CategoriaNombre


class Producto(models.Model):
    ProductoId = models.AutoField(primary_key = True, verbose_name = 'ID')
    ProductoCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name = 'Categoria')
    ProductoNombre = models.CharField(max_length=200 , verbose_name = 'Nombre del producto',unique = True)
    ProductoPrecio= models.DecimalField(max_digits=10, decimal_places=2,verbose_name = 'Precio')
    ProductoImagen = models.ImageField(upload_to ='uploads/',default = 'uploads/None/no-img.jpg,',verbose_name = 'Imagen') 
    def __str__(self):
        """
        String que representa al objeto Producto
        """
        return self.ProductoNombre
