# Generated by Django 4.0.4 on 2022-05-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_pod_podmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pod',
            name='code',
            field=models.SmallIntegerField(max_length=5, unique=True),
        ),
    ]
