# Generated by Django 5.0.2 on 2024-03-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0020_mdesign_mimage2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mdesign2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mimage2', models.ImageField(upload_to='static/uploads/')),
            ],
        ),
        migrations.RemoveField(
            model_name='mdesign',
            name='mimage2',
        ),
    ]
