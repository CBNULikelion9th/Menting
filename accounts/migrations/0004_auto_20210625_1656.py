# Generated by Django 3.2 on 2021-06-25 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_studenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='entrancetype',
            field=models.CharField(default='멘토만 작성', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='highschool',
            field=models.CharField(default='멘토만 작성', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='major',
            field=models.CharField(default='멘토만 작성', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='university',
            field=models.CharField(default='멘토만 작성', max_length=50),
        ),
    ]