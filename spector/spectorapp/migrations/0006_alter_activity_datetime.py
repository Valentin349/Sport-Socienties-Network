# Generated by Django 4.0.2 on 2022-03-09 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectorapp', '0005_alter_activity_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 9, 20, 3, 54, 342313)),
        ),
    ]
