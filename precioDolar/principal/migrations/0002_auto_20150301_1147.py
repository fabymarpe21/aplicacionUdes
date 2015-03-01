# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolar',
            name='precios',
            field=djorm_pgarray.fields.ArrayField(dbtype=b'text', dimension=2),
        ),
    ]
