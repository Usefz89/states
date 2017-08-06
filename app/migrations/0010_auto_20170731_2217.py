# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='county',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='app.State', null=True),
        ),
    ]
