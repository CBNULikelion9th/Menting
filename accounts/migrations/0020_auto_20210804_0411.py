# Generated by Django 3.2.6 on 2021-08-04 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20210702_0728'),
    ]

    operations = [
        migrations.DeleteModel(
            name='University',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]