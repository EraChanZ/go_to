# Generated by Django 2.1 on 2018-08-17 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180817_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dann',
            name='created',
        ),
        migrations.RemoveField(
            model_name='dann',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='dann',
            name='kluch',
        ),
    ]
