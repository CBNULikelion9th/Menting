# Generated by Django 3.2.4 on 2021-06-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post2_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post2',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post2',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
