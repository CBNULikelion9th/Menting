# Generated by Django 3.2 on 2021-06-29 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menteerequest', '0003_alter_mentee_request_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentee_request',
            old_name='creadted_at',
            new_name='created_at',
        ),
    ]