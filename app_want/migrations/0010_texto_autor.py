# Generated by Django 3.0.7 on 2020-08-02 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_want', '0009_remove_usuario_senha'),
    ]

    operations = [
        migrations.AddField(
            model_name='texto',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_want.usuario'),
            preserve_default=False,
        ),
    ]
