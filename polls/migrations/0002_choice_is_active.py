# Generated by Django 5.1.2 on 2024-10-30 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
