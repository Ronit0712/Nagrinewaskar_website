# Generated by Django 5.0.2 on 2024-03-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0014_achievementmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=15)),
            ],
        ),
    ]
