# Generated by Django 5.1.2 on 2024-10-31 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='q_text',
            new_name='question_text',
        ),
    ]
