# Generated by Django 3.1.1 on 2023-05-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]