# Generated by Django 3.2.6 on 2021-08-11 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_recomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='university',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]