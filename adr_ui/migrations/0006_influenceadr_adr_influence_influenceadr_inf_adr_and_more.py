# Generated by Django 4.0.5 on 2022-06-11 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adr_ui', '0005_influence_remove_adr_when adr was created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluenceADR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changedAt', models.DateTimeField(auto_now_add=True, db_column='changedAt')),
            ],
        ),
        migrations.AddField(
            model_name='adr',
            name='influence',
            field=models.ManyToManyField(through='adr_ui.InfluenceADR', to='adr_ui.adr'),
        ),
        migrations.AddField(
            model_name='influenceadr',
            name='inf_adr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adr_ui.adr'),
        ),
        migrations.AddField(
            model_name='influenceadr',
            name='influence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adr_ui.influence'),
        ),
    ]