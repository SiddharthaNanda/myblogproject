# Generated by Django 3.0.3 on 2020-06-24 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200624_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 11, 38, 3, 579158, tzinfo=utc)),
        ),
    ]
