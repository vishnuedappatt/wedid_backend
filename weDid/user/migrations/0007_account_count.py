# Generated by Django 4.1 on 2022-08-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_delete_jobportal'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]