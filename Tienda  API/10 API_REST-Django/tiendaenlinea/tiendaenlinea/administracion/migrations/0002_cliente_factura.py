# Generated by Django 3.2.9 on 2021-11-18 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_Factura', models.CharField(max_length=9, unique=True)),
                ('fecha_venta', models.DateTimeField()),
                ('cliente_asociado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='administracion.cliente')),
                ('productos', models.ManyToManyField(to='administracion.Producto')),
            ],
        ),
    ]