# Generated by Django 5.0.6 on 2024-06-05 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0004_formulir_pendaftar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pengguna.pendafatar'),
        ),
    ]
