# Generated by Django 5.0.2 on 2024-03-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0011_gallerys4model'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitysliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actimage', models.ImageField(upload_to='static/uploads/')),
                ('acttitle', models.CharField(max_length=100)),
            ],
        ),
    ]
