# Generated by Django 4.1.6 on 2023-02-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_plot_contour'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='plot_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
