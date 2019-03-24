# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("djangocms_versioning", "0005_remove_version_label"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="version", unique_together=set([("content_type", "object_id")])
        )
    ]
