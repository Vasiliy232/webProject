# Generated by Django 4.2 on 2023-04-28 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_structure_registers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='data_type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.datatype'),
        ),
        migrations.AlterField(
            model_name='substructure',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.structure'),
        ),
    ]
