# Generated by Django 3.2 on 2021-07-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_customuser_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='university',
            field=models.CharField(default='멘토만 작성', max_length=50),
        ),
        migrations.AlterField(
            model_name='university',
            name='univer',
            field=models.CharField(max_length=50),
        ),
    ]
