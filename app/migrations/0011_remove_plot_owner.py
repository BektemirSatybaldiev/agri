# Generated by Django 4.1.6 on 2023-02-12 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_plot_plot_id_farmer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='owner',
        ),
    ]
