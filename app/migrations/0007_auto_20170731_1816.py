# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170731_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecapital',
            name='latitude',
            field=models.FloatField(null=True),
        ),
    ]
