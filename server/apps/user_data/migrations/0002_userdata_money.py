# Generated by Django 5.0.4 on 2024-04-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='money',
            field=models.IntegerField(default=0),
        ),
    ]
