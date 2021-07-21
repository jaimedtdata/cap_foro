# Generated by Django 3.2 on 2021-07-20 15:50

import apps.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area_interest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(help_text='Nombre de Area', max_length=200, verbose_name='Area')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Areas de Interes',
            },
        ),
        migrations.CreateModel(
            name='Categories_foro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(help_text='Nombre de Categoria', max_length=200, verbose_name='Nombre de Categoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Foro Categorias',
            },
        ),
        migrations.CreateModel(
            name='Categories_Normas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(help_text='Nombre de Plan', max_length=200, verbose_name='Nombre de la Categoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Normas - Categorias',
            },
        ),
        migrations.CreateModel(
            name='coments_foro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coments', models.CharField(help_text='comentario', max_length=200, verbose_name='comentario')),
                ('validity_date_start', models.DateTimeField(help_text='Fecha Inicio', verbose_name='Fecha Fin')),
                ('validity_date_finish', models.DateTimeField(help_text='Fecha Inicio', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Foro Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Location_Normas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Location_name', models.CharField(help_text='Nombre de Plan', max_length=200, verbose_name='Plan')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Normas - Locacion',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('planame', models.CharField(help_text='Nombre de Plan', max_length=200, verbose_name='Plan')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validity_date_start', models.DateField(help_text='Fecha', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Planes de Suscripcion',
            },
        ),
        migrations.CreateModel(
            name='Policies_usage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Titulo de Consulta', max_length=200, verbose_name='Titulo de Consulta')),
                ('message', models.TextField(help_text='Respuesta', verbose_name='Respuesta')),
                ('platform', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validity_date_start', models.DateField(help_text='Fecha', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Preguntas Frecuentes',
            },
        ),
        migrations.CreateModel(
            name='Subcategories_foro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(help_text='Subcategoria', max_length=200, verbose_name='Subcategoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Foro SubCategorias',
            },
        ),
        migrations.CreateModel(
            name='Subcategories_Normas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(help_text='Nombre de Plan', max_length=200, verbose_name='Plan')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Normas - SubCategoria',
            },
        ),
        migrations.CreateModel(
            name='themas_foro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('themas_name', models.CharField(help_text='Nombre de Tema', max_length=200, verbose_name='Plan')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Foro Temas',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='Nombre completo', help_text='Apellidos y Nombres', max_length=200, verbose_name='Apellidos y Nombres')),
                ('names', models.CharField(help_text='Nombres O Razón Social', max_length=50, verbose_name='Nombres')),
                ('first_surname', models.CharField(blank=True, help_text='Primer Apellido', max_length=50, verbose_name='Primer Apellido')),
                ('second_surname', models.CharField(blank=True, help_text='Segundo Apellido', max_length=50, verbose_name='Segundo Apellido')),
                ('person_type', models.CharField(choices=[('N', 'NATURAL'), ('J', 'JURÍDICA')], default='N', help_text='Tipo de Persona', max_length=1, verbose_name='Tipo de Persona')),
                ('identity', models.CharField(blank=True, help_text='DNI o RUC', max_length=11, verbose_name='Documento de Identidad')),
                ('profession', models.CharField(blank=True, choices=[('A', 'ARQUITECTO'), ('I', 'INGENIERO')], help_text='Profesión', max_length=1, verbose_name='Profesión')),
                ('mobile', models.CharField(blank=True, help_text='Número de Teléfono Celular', max_length=12, verbose_name='Celular')),
                ('phone', models.CharField(blank=True, help_text='Número de Teléfono Fijo o de Oficina', max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(default='correo@dominio.com', help_text='Correo Electrónico', max_length=50, verbose_name='Email')),
                ('tuition', models.PositiveIntegerField(blank=True, help_text='Colegiatura', null=True, verbose_name='Colegiatura')),
                ('secret_code', models.PositiveIntegerField(blank=True, help_text='Código Secreto de Arquitecto', null=True, verbose_name='Código Secreto de Arquitecto')),
                ('address', models.CharField(blank=True, help_text='Dirección', max_length=200, verbose_name='Dirección')),
                ('photo', models.ImageField(blank=True, help_text='Suba una fotografía en tamaño pasaporte o carnet', null=True, upload_to=apps.models.upload_photos, verbose_name='Fotografía')),
                ('area_interest', models.CharField(blank=True, help_text='areas de interes', max_length=200, verbose_name='areas de interes')),
                ('institution', models.CharField(blank=True, help_text='Institucion', max_length=200, verbose_name='Institucion')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('user', models.OneToOneField(blank=True, help_text='Usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Relacion de Miembros',
            },
        ),
        migrations.CreateModel(
            name='Master_Normas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(help_text='Registro de Locacion', max_length=200, verbose_name='Locacion')),
                ('validity_date_start', models.DateField(help_text='Fecha Publicacion', verbose_name='Fecha Publicacion')),
                ('keywords', models.CharField(help_text='Palabras Clave', max_length=200, verbose_name='Registre palabras clave')),
                ('file', models.FileField(help_text='Suba el archivo o base legal', upload_to=apps.models.upload_file, verbose_name='File')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('category_name', models.ForeignKey(help_text='registro de Categoria', on_delete=django.db.models.deletion.CASCADE, to='apps.categories_normas', verbose_name='Categoria')),
                ('subcategory_name', models.ForeignKey(help_text='registro de SubCategoria', on_delete=django.db.models.deletion.CASCADE, to='apps.subcategories_normas', verbose_name='SubCategoria')),
            ],
            options={
                'verbose_name_plural': 'Normas - Registro Principal',
            },
        ),
        migrations.CreateModel(
            name='Control_payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Id_user', models.CharField(help_text='iduser', max_length=200, verbose_name='Plan')),
                ('pay_method', models.CharField(help_text='Metodo Pago', max_length=200, verbose_name='Metodo Pago')),
                ('pay_import', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validity_date_start', models.DateField(help_text='Fecha', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('Id_plan', models.OneToOneField(blank=True, help_text='Plan Suscrito', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.plan', verbose_name='Plan de Suscripcion')),
                ('member', models.OneToOneField(blank=True, help_text='Miembros', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.member', verbose_name='Miembros')),
            ],
            options={
                'verbose_name_plural': 'Control de Pagos',
            },
        ),
    ]
