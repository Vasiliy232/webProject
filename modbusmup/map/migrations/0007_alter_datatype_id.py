# Generated by Django 4.2 on 2023-04-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_alter_register_data_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
