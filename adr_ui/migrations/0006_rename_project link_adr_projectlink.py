# Generated by Django 4.0.5 on 2022-06-11 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adr_ui', '0005_rename_affected solutions_adr_affectedsolutions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adr',
            old_name='Project Link',
            new_name='projectLink',
        ),
    ]
