# Generated by Django 4.2.7 on 2023-12-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newAI_app', '0002_chatlog_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]