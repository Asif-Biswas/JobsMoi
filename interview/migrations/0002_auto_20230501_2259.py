# Generated by Django 3.1.1 on 2023-05-01 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewcomment',
            old_name='discussion',
            new_name='interview',
        ),
    ]
