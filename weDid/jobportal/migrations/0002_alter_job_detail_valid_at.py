# Generated by Django 4.1 on 2022-09-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_detail',
            name='valid_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
