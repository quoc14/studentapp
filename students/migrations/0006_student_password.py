# Generated by Django 5.2 on 2025-06-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_tuitionrecord_proof_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
