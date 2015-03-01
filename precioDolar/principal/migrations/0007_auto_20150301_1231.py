# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20150301_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolar',
            name='precios',
            field=models.TextField(),
        ),
    ]
