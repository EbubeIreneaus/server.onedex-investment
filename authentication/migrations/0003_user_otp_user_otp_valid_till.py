# Generated by Django 5.0.7 on 2024-07-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='OTP',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='OTP_VALID_TILL',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
