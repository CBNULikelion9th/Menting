# Generated by Django 3.2 on 2021-07-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muniver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('univer', models.CharField(max_length=50)),
            ],
        ),
    ]