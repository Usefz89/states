# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170731_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statecapital',
            name='state',
        ),
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, to='app.State'),
        ),
    ]
