# Generated by Django 5.0.2 on 2024-02-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
            ],
        ),
    ]
