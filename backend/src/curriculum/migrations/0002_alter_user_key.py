# Generated by Django 5.0.4 on 2024-04-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.CharField(default='gZ4vkyc6K8apOlo4D51S', max_length=20),
        ),
    ]
