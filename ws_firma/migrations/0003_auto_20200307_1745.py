# Generated by Django 3.0.3 on 2020-03-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_firma', '0002_auto_20200305_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='error',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='documento',
            name='estado',
            field=models.CharField(choices=[('A', 'Autorizado'), ('P', 'Pendiente'), ('N', 'Negado')], default='P', max_length=1),
        ),
    ]