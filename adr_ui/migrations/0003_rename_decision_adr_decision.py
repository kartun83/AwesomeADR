# Generated by Django 4.0.5 on 2022-06-11 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adr_ui', '0002_adr_decision status_adr_effects_adr_decision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adr',
            old_name='decision',
            new_name='Decision',
        ),
    ]
