# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20150301_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolar',
            name='precios',
            field=models.DateField(),
        ),
    ]
