# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Robb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='host_groups',
        ),
        migrations.RemoveField(
            model_name='action',
            name='hosts',
        ),
        migrations.RemoveField(
            model_name='action',
            name='operations',
        ),
        migrations.RemoveField(
            model_name='action',
            name='triggers',
        ),
        migrations.RemoveField(
            model_name='actionoperation',
            name='notifiers',
        ),
        migrations.RemoveField(
            model_name='host',
            name='host_groups',
        ),
        migrations.RemoveField(
            model_name='host',
            name='templates',
        ),
        migrations.RemoveField(
            model_name='hostgroup',
            name='templates',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='host_groups',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='hosts',
        ),
        migrations.RemoveField(
            model_name='service',
            name='items',
        ),
        migrations.RemoveField(
            model_name='template',
            name='services',
        ),
        migrations.RemoveField(
            model_name='template',
            name='triggers',
        ),
        migrations.RemoveField(
            model_name='triggerexpression',
            name='service',
        ),
        migrations.RemoveField(
            model_name='triggerexpression',
            name='service_index',
        ),
        migrations.RemoveField(
            model_name='triggerexpression',
            name='trigger',
        ),
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='ActionOperation',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.DeleteModel(
            name='HostGroup',
        ),
        migrations.DeleteModel(
            name='Maintenance',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceIndex',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
        migrations.DeleteModel(
            name='Trigger',
        ),
        migrations.DeleteModel(
            name='TriggerExpression',
        ),
    ]
