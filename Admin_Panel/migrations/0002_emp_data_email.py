# Generated by Django 5.1.1 on 2024-09-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_data',
            name='Email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]
