# Generated by Django 4.2.1 on 2023-06-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCorrea', '0005_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_basico',
            name='estado_pedido',
            field=models.CharField(default='Pendiente', max_length=50),
        ),
    ]