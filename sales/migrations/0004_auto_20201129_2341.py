# Generated by Django 3.1.3 on 2020-11-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20201129_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleorderline',
            options={'verbose_name': 'Linea de Orden de Venta', 'verbose_name_plural': 'Lineas de Ordenes de Venta'},
        ),
        migrations.RenameField(
            model_name='saleorderline',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='total_amount',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='saleorderline',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
