# Generated by Django 4.0.5 on 2022-06-11 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adr_ui', '0007_status_color_status_mark_alter_status_description'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='influenceadr',
            unique_together=set(),
        ),
    ]
