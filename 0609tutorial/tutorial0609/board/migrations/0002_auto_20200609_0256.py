# Generated by Django 3.0.7 on 2020-06-09 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='sytle',
            new_name='style',
        ),
        migrations.RenameField(
            model_name='board',
            old_name='tittle',
            new_name='title',
        ),
    ]