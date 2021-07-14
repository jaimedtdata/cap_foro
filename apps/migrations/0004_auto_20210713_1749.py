# Generated by Django 3.2 on 2021-07-13 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20210713_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_normas',
            name='category_name',
            field=models.ForeignKey(help_text='registro de Categoria', on_delete=django.db.models.deletion.CASCADE, to='apps.categories_normas', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='master_normas',
            name='subcategory_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.subcategories_normas'),
        ),
    ]