# Generated by Django 3.2.4 on 2021-06-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
