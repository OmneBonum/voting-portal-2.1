# Generated by Django 4.0.4 on 2022-07-28 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0018_rename_delegated_podmember_put_farward_recipient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pod',
            old_name='inivitation_code',
            new_name='invitation_code',
        ),
    ]
