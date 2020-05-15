# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-15 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eyeaux', '0004_auto_20161025_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhsbtlog',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eyeaux.NHSBTFile'),
        ),
        migrations.AlterField(
            model_name='nhsbtlog',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eyeaux.NHSBTRecord'),
        ),
        migrations.AlterField(
            model_name='psslimsresult',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eyeaux.PSSPerson'),
        ),
        migrations.AlterField(
            model_name='pssmicroresult',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eyeaux.PSSPerson'),
        ),
    ]