# Generated by Django 4.0.4 on 2022-05-16 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0013_podmember_vote_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podmember',
            name='vote_in',
        ),
        migrations.RemoveField(
            model_name='podmember',
            name='vote_out',
        ),
        migrations.CreateModel(
            name='PodMember_vote_out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.podmember')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
