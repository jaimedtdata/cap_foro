# Generated by Django 3.2 on 2021-07-21 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_normas',
            name='Location_name',
            field=models.CharField(help_text='Nombre Locacion', max_length=200, verbose_name='Locacion'),
        ),
        migrations.AlterField(
            model_name='master_normas',
            name='location_name',
            field=models.ForeignKey(help_text='Registro de Locacion', on_delete=django.db.models.deletion.CASCADE, to='apps.location_normas', verbose_name='Locacion'),
        ),
        migrations.AlterField(
            model_name='policies_usage',
            name='platform',
            field=models.CharField(choices=[('F', 'FORO'), ('N', 'NORMAS')], help_text='Plataforma', max_length=1, verbose_name='Plataforma'),
        ),
    ]