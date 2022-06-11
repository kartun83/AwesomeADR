# Generated by Django 4.0.5 on 2022-06-11 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adr_ui', '0004_alter_influenceadr_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adr',
            old_name='Affected solutions',
            new_name='affectedSolutions',
        ),
        migrations.RenameField(
            model_name='adr',
            old_name='Decision context',
            new_name='decContext',
        ),
        migrations.RenameField(
            model_name='adr',
            old_name='Decision status',
            new_name='decStatus',
        ),
        migrations.RenameField(
            model_name='adr',
            old_name='Decision',
            new_name='decision',
        ),
        migrations.RenameField(
            model_name='adr',
            old_name='Effects',
            new_name='effects',
        ),
        migrations.RenameField(
            model_name='adr',
            old_name='When status was changed',
            new_name='statusChangedAt',
        ),
    ]
