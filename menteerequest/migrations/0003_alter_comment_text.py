# Generated by Django 3.2 on 2021-06-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteerequest', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True),
        ),
    ]