# Generated by Django 3.2.4 on 2021-07-22 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_recomment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recomment',
            name='post',
        ),
    ]
