# Generated by Django 3.2.4 on 2021-07-13 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_recomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomment',
            name='name2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recomment',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]