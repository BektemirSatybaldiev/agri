# Generated by Django 4.1.6 on 2023-02-11 17:33

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_plot_contour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='contour',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]
