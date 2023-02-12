# Generated by Django 4.1.6 on 2023-02-12 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_plot_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='plot_id',
        ),
        migrations.AddField(
            model_name='farmer',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
