# Generated by Django 5.0.7 on 2025-01-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_doner_alter_event_user_delete_accepteddoner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
