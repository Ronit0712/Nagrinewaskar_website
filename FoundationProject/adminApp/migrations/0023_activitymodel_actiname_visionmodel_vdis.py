# Generated by Django 5.0.2 on 2024-03-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0022_remove_activitymodel_actiname'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitymodel',
            name='actiname',
            field=models.CharField(default='true', max_length=100),
        ),
        migrations.AddField(
            model_name='visionmodel',
            name='vdis',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
