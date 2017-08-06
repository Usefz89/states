# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170731_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='app.State'),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(to='app.State'),
        ),
    ]
