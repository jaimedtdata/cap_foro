# Generated by Django 3.2 on 2021-07-20 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='control_payment',
            name='Id_user',
        ),
    ]
