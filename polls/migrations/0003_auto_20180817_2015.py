# Generated by Django 2.1 on 2018-08-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_dann'),
    ]

    operations = [
        migrations.AddField(
            model_name='dann',
            name='created',
            field=models.DateField(default='2018-08-17'),
        ),
        migrations.AddField(
            model_name='dann',
            name='due_date',
            field=models.DateField(default='2018-08-17'),
        ),
        migrations.AddField(
            model_name='dann',
            name='kluch',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
