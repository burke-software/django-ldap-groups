# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='LDAPGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('make_staff', models.BooleanField(default=False)),
                ('make_superuser', models.BooleanField(default=False)),
                ('org_unit', models.TextField()),
                ('groups', models.ManyToManyField(related_name='ldap_org_units', to='auth.Group')),
            ],
            options={
                'ordering': ['org_unit'],
            },
        ),
    ]
