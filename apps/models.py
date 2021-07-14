from django.db import models
from .choices import *
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User

def upload_file(instance, filename):
    ext = filename.split('.')[-1]
    return 'pdf/{}'.format(instance.file)

def upload_signature(instance, filename):
    ext = filename.split('.')[-1]
    return 'signatures/{}.{}'.format(instance.file, ext)

def upload_photos(instance, filename):
    ext = filename.split('.')[-1]
    return 'photos/{}.{}'.format(instance.identity, ext)



"""

 * TABLAS GENERALES 

"""



class Member(models.Model):
    user = models.OneToOneField(
		User, on_delete=models.CASCADE,
		help_text='Usuario', null=True, blank=True,
		verbose_name='Usuario')
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, blank=False,default='Nombre completo',
        help_text='Apellidos y Nombres',
        verbose_name='Apellidos y Nombres')
    names = models.CharField(max_length=50, blank=False,
        help_text='Nombres O Razón Social',
        verbose_name='Nombres')
    first_surname = models.CharField(max_length=50, blank=True,
        help_text='Primer Apellido',
        verbose_name='Primer Apellido')
    second_surname = models.CharField(max_length=50, blank=True,
        help_text='Segundo Apellido',
        verbose_name='Segundo Apellido')
    person_type = models.CharField(max_length=1, default='N',
        help_text='Tipo de Persona', choices=PERSON_TYPE_CHOICES,
        verbose_name='Tipo de Persona', blank=False)
    identity = models.CharField(max_length=11, blank=True,
        help_text='DNI o RUC',
        verbose_name='Documento de Identidad')
    profession = models.CharField(max_length=1,
        help_text='Profesión', choices=PROFESSION_CHOICES,
        verbose_name='Profesión', blank=True)
    mobile = models.CharField(max_length=12, blank=True,
        help_text='Número de Teléfono Celular',
        verbose_name='Celular')
    phone = models.CharField(max_length=10, blank=True,
        help_text='Número de Teléfono Fijo o de Oficina',
        verbose_name='Teléfono')
    email = models.EmailField(max_length=50, blank=False,default='correo@dominio.com',
        help_text='Correo Electrónico',
        verbose_name='Email')
    tuition = models.PositiveIntegerField(null=True, blank=True,
        help_text='Colegiatura',
        verbose_name='Colegiatura')
    secret_code = models.PositiveIntegerField(null=True, blank=True,
        help_text='Código Secreto de Arquitecto',
        verbose_name='Código Secreto de Arquitecto')
    address = models.CharField(max_length=200, blank=True,
        help_text='Dirección',
        verbose_name='Dirección')
    is_signature_validated = models.BooleanField(default=False,
        help_text='Marcado si la firma está validada por el CAP',
        verbose_name='Firma Validada')
    signature = models.ImageField(
        upload_to=upload_signature, blank=False,
        help_text='Suba una imágen escaneada de su sello y firma, los cuales será utilizados como validación de las solicitudes que realice através del portal',
        verbose_name='Firma')
    photo = models.ImageField(
        upload_to=upload_photos, blank=True, null=True,
        help_text='Suba una fotografía en tamaño pasaporte o carnet',
        verbose_name='Fotografía')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    area_interest = models.CharField(max_length=200, blank=True,
        help_text='areas de interes',
        verbose_name='areas de interes')
    institution = models.CharField(max_length=200, blank=True,
        help_text='Institucion',
        verbose_name='Institucion')
    
    def __str__(self):
        return self.firstname + " " + self.lastname
 
    class Meta:
        ordering = ['created']
         
    class Meta:  
        db_table = "member"

    class Meta:
        verbose_name_plural = 'Relacion de Miembros'

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    planame = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')      
    cost = models.DecimalField(max_digits = 10,decimal_places = 2)
    validity_date_start = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Inicio')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    
    class Meta:
        verbose_name_plural = 'Planes de Suscripcion'



class Control_payment(models.Model):
    id = models.AutoField(primary_key=True)
    Id_plan = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')    
    Id_user = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')          
    pay_method =  models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')  
    pay_import = models.DecimalField(max_digits = 10,decimal_places = 2)
    validity_date_start = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Inicio')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Control de Pagos'

"""

 * TABLAS NORMAS 

"""


class Policies_usage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False,
        help_text='Titulo de Consulta',
        verbose_name='Titulo de Consulta')      
    message = models.TextField(blank=False,
        help_text='Respuesta',
        verbose_name='Respuesta')      
    platform = models.DecimalField(max_digits = 10,decimal_places = 2)
    validity_date_start = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Inicio')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Preguntas Frecuentes'



class Categories_Normas(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Nombre de la Categoria')      

    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    
    class Meta:
        verbose_name_plural = 'Normas - Categorias'
    def __str__(self):
        return self.category_name
    

class Subcategories_Normas(models.Model):
    id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Normas - SubCategoria'
    def __str__(self):
        return self.subcategory_name    

class Location_Normas(models.Model):
    id = models.AutoField(primary_key=True)
    Location_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Normas - Locacion'

class Master_Normas(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.ForeignKey(Categories_Normas, on_delete=models.CASCADE,
        help_text='registro de Categoria',
        verbose_name='Categoria')     
    subcategory_name = models.ForeignKey(Subcategories_Normas, on_delete=models.CASCADE,
        help_text='registro de SubCategoria',
        verbose_name='SubCategoria')     
    location_name = models.CharField(max_length=200, blank=False,
        help_text='Registro de Locacion',
        verbose_name='Locacion')          
    validity_date_start = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Inicio')
    validity_date_finish = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Fin',
        verbose_name='Fecha Fin')
    keywords = models.CharField(max_length=200, blank=False,
        help_text='Palabras Clave',
        verbose_name='Registre palabras clave') 
    file = models.FileField(
        upload_to=upload_file, blank=False,
        help_text='Suba el archivo o base legal',
        verbose_name='File')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Normas - Registro Principal'

"""

 * TABLAS FORO 

"""


class Area_interest(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Area',
        verbose_name='Area')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Areas de Interes'



class Categories_foro(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')      
    validity_date_start = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Foro Categorias'


class Subcategories_foro(models.Model):
    id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')      
    validity_date_start = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Foro SubCategorias'



class themas_foro(models.Model):
    id = models.AutoField(primary_key=True)
    Location_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')      
    validity_date_start = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Foro Temas'


class coments_foro(models.Model):
    id = models.AutoField(primary_key=True)
    coments = models.CharField(max_length=200, blank=False,
        help_text='comentario',
        verbose_name='comentario')      
    validity_date_start = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Foro Comentarios'


"""
"Registartions
 Attributes of Registartions are registration_id,registration_user_id,registration_name, registration_type,registration_number, registration_date,registration_description"

"Posts :
 post_id,post_user_id,post_title,post_type, post_description"

"Replies :
 replies_id, replies_user_id,replies_title, replies_type,replies_description"

"Polls Entity : Attributes of Polls are poll_id,poll_name, pon_type, poll_description"
https://github.com/mdn/django-diy-blog/blob/master/blog/models.py
"""