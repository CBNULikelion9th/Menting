# Generated by Django 3.2 on 2021-06-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteerequest', '0004_rename_creadted_at_mentee_request_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee_request',
            name='grade',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('기타', '기타')], max_length=2),
        ),
    ]
