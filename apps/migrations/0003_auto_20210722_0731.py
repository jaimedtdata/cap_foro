# Generated by Django 3.2 on 2021-07-22 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20210721_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master_normas',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='master_normas',
            name='location_name',
        ),
        migrations.RemoveField(
            model_name='master_normas',
            name='subcategory_name',
        ),
        migrations.DeleteModel(
            name='Categories_Normas',
        ),
        migrations.DeleteModel(
            name='Location_Normas',
        ),
        migrations.DeleteModel(
            name='Master_Normas',
        ),
        migrations.DeleteModel(
            name='Subcategories_Normas',
        ),
    ]