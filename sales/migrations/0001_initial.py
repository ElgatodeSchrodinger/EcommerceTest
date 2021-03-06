# Generated by Django 3.1.3 on 2020-11-29 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la categoría')),
                ('icon', models.ImageField(upload_to='sales/categories')),
                ('parent_categ_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.category')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres')),
                ('lastname', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('identification_number', models.CharField(max_length=20, verbose_name='DNI')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del Producto')),
                ('image', models.ImageField(upload_to='sales/products')),
                ('price', models.FloatField(verbose_name='Precio del Producto')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('categ_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('state', models.CharField(choices=[('cart', 'En Carrito'), ('process', 'Procesado'), ('cancel', 'Cancelado')], default='cart', max_length=10, verbose_name='Estado')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('total_amount', models.FloatField(verbose_name='Precio Total')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.customer', verbose_name='Cliente')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Orden de Venta',
                'verbose_name_plural': 'Ordenes de Venta',
            },
        ),
    ]
