# Generated by Django 5.0.2 on 2024-03-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0005_valuesmoddel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisioncardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcdis', models.TextField()),
                ('vcimage', models.ImageField(upload_to='static/uploads/')),
                ('vcimgtitle', models.CharField(max_length=100)),
            ],
        ),
    ]
