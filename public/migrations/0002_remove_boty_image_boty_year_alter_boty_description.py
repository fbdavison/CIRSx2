# Generated by Django 5.0 on 2024-09-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boty',
            name='image',
        ),
        migrations.AddField(
            model_name='boty',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boty',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
