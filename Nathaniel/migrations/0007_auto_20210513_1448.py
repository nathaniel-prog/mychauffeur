# Generated by Django 3.1.3 on 2021-05-13 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nathaniel', '0006_auto_20210513_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='chauffeur',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 13, 14, 48, 56, 447987)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 13, 14, 48, 56, 447987)),
        ),
    ]
