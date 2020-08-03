# Generated by Django 3.0.7 on 2020-08-02 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_want', '0005_auto_20200802_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='texto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='titulo')),
                ('corpo', models.CharField(max_length=800, verbose_name='corpo')),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_want.wanted')),
            ],
        ),
    ]