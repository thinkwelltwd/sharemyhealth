# Generated by Django 2.1.2 on 2019-04-08 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hixny', '0006_hixnyprofile_terms_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hixnyprofile',
            name='cda_file',
        ),
        migrations.RemoveField(
            model_name='hixnyprofile',
            name='step_1',
        ),
        migrations.RemoveField(
            model_name='hixnyprofile',
            name='step_2',
        ),
        migrations.RemoveField(
            model_name='hixnyprofile',
            name='step_3',
        ),
        migrations.RemoveField(
            model_name='hixnyprofile',
            name='step_4',
        ),
        migrations.RemoveField(
            model_name='hixnyprofile',
            name='step_5',
        ),
    ]
