# Generated by Django 3.2 on 2021-06-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_studentnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='studenttype',
            field=models.BooleanField(default=False),
        ),
    ]
