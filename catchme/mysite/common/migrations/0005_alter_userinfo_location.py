# Generated by Django 4.2.3 on 2024-03-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_matchinghistory_delete_matchinginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
