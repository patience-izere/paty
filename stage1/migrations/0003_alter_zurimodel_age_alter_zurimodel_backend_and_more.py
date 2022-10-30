# Generated by Django 4.1.2 on 2022-10-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage1', '0002_alter_zurimodel_age_alter_zurimodel_backend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zurimodel',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='zurimodel',
            name='backend',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='zurimodel',
            name='slackUsername',
            field=models.CharField(max_length=200),
        ),
    ]
