# Generated by Django 4.1.2 on 2022-11-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0008_rename_judgements_ipc_judgements_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipc_judgements',
            name='ipc_judgements_description',
        ),
        migrations.AddField(
            model_name='ipc_judgements',
            name='ipc_judgements_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ipc_judgements',
            name='ipc_judgements_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
