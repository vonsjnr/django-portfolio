# Generated by Django 3.1.5 on 2021-01-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/projects/img'),
        ),
    ]
