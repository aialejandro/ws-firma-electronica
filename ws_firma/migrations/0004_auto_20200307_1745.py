# Generated by Django 3.0.3 on 2020-03-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_firma', '0003_auto_20200307_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='error',
            field=models.TextField(),
        ),
    ]
