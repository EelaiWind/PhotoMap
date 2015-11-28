# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationMarker', '0002_demophoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='demophoto',
            name='title',
            field=models.CharField(default='title', max_length=30),
            preserve_default=False,
        ),
    ]
