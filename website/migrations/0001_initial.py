# Generated by Django 3.1.7 on 2021-02-22 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('CategoriaId', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoriaNombre', models.CharField(max_length=200, unique=True, verbose_name='Nombre de categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('ProductoId', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductoNombre', models.CharField(max_length=200, unique=True, verbose_name='Nombre del producto')),
                ('ProductoPrecio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ProductoCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.categoria')),
            ],
        ),
    ]
