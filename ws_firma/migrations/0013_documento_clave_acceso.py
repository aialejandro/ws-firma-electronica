# Generated by Django 3.0.4 on 2020-07-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_firma', '0012_documento_documento_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='clave_acceso',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
