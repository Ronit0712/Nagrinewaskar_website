# Generated by Django 5.0.2 on 2024-03-12 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0007_historymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallerys1model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1img', models.ImageField(upload_to='static/uploads/')),
            ],
        ),
    ]
