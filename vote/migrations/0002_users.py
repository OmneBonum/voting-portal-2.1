# Generated by Django 4.0.4 on 2022-05-11 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reg', models.BooleanField(default=False)),
                ('verificationScore', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('userType', models.PositiveSmallIntegerField(default=0)),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('voterID', models.IntegerField(blank=True, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vote.districts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
