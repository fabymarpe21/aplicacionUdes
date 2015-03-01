# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20150301_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolar',
            name='precios',
            field=models.CharField(max_length=128),
        ),
    ]
