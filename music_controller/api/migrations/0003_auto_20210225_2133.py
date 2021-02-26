# Generated by Django 3.1.6 on 2021-02-25 16:33

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210216_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
