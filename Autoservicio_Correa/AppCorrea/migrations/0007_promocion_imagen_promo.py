# Generated by Django 4.2.1 on 2023-06-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCorrea', '0006_pedido_basico_estado_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='imagen_promo',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_promo'),
        ),
    ]
