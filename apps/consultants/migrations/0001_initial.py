# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('longUniqueTWNumber', models.CharField(serialize=False, max_length=20, primary_key=True, unique=True)),
                ('ship', models.CharField(max_length=4)),
                ('team', models.CharField(max_length=2)),
                ('number', models.CharField(max_length=4)),
                ('position', models.CharField(max_length=2)),
                ('y', models.CharField(max_length=1)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('zipCode', models.CharField(max_length=4)),
                ('town', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('phone1', models.CharField(max_length=8)),
                ('phone2', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=100)),
                ('y2', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='consultant',
            unique_together=set([('number', 'firstName', 'lastName')]),
        ),
    ]
