# Generated by Django 2.1.1 on 2018-09-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
