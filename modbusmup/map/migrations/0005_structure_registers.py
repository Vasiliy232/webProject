# Generated by Django 4.2 on 2023-04-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_register_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='registers',
            field=models.ManyToManyField(to='map.register'),
        ),
    ]
