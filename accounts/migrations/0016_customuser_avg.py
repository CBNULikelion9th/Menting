# Generated by Django 3.2 on 2021-07-01 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_customuser_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avg',
            field=models.IntegerField(default=0),
        ),
    ]
