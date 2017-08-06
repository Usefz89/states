# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170731_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecapital',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='population',
            field=models.IntegerField(null=True),
        ),
    ]
