# Generated by Django 4.0.5 on 2022-06-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adr_ui', '0006_rename_project link_adr_projectlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='color',
            field=models.CharField(db_column='color', default='', max_length=20, verbose_name='Coloring for puml'),
        ),
        migrations.AddField(
            model_name='status',
            name='mark',
            field=models.CharField(db_column='mark', default='', max_length=1, verbose_name='Header mark for puml'),
        ),
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.TextField(db_column='description', verbose_name='Description'),
        ),
    ]