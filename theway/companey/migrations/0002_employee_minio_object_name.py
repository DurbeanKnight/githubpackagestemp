# Generated by Django 4.1 on 2023-12-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='minio_object_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
