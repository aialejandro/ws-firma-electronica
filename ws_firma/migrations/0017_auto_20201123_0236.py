# Generated by Django 3.1.3 on 2020-11-23 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ws_firma', '0016_documento_clave_acceso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='autorizacion',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='clave_acceso',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='documento_tipo',
        ),
    ]
