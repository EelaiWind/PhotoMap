# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationMarker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100)),
                ('marker', models.ForeignKey(to='LocationMarker.Marker')),
            ],
        ),
    ]
