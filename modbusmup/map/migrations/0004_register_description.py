# Generated by Django 4.2 on 2023-04-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_datatype_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
