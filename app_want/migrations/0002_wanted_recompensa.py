# Generated by Django 3.0.7 on 2020-07-22 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_want', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wanted',
            name='recompensa',
            field=models.FloatField(default=-1.0, verbose_name='Berries'),
            preserve_default=False,
        ),
    ]