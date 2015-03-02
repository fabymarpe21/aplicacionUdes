# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20150301_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolar',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dolar',
            name='precios',
            field=models.CharField(max_length=500),
        ),
    ]
