from django.db import models
from apps.choices import *
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
# Create your models here.




def upload_file(instance, filename):
    ext = filename.split('.')[-1]
    return 'pdf/{}'.format(instance.file)

def upload_signature(instance, filename):
    ext = filename.split('.')[-1]
    return 'signatures/{}.{}'.format(instance.file, ext)

def upload_photos(instance, filename):
    ext = filename.split('.')[-1]
    return 'photos/{}.{}'.format(instance.identity, ext)



class Categories_Normas(models.Model):
    
    category_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Categoria',
        verbose_name='Nombre de la Categoria')      

    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    
    class Meta:
        verbose_name_plural = '1.Normas - Categorias'
    def __str__(self):
        return self.category_name



class Subcategories_Normas(models.Model):
    
    subcategory_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de sub Categoria',
        verbose_name='sub Categoria')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '2.Normas - SubCategoria'
    def __str__(self):
        return self.subcategory_name    

class Location_Normas(models.Model):
    
    Location_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre Locacion',
        verbose_name='Locacion')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '3.Normas - Locacion'

class Master_Normas(models.Model):
    
    category_name = models.ForeignKey(Categories_Normas, on_delete=models.CASCADE,
        help_text='registro de Categoria',
        verbose_name='Categoria')     
    subcategory_name = models.ForeignKey(Subcategories_Normas, on_delete=models.CASCADE,
        help_text='registro de SubCategoria',
        verbose_name='SubCategoria')     
    location_name =  models.ForeignKey(Location_Normas, on_delete=models.CASCADE,
        help_text='Registro de Locacion',
        verbose_name='Locacion')
    norma_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre Norma',
        verbose_name='Norma')                
    validity_date_start = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Publicacion',
        verbose_name='Fecha Publicacion')
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
        verbose_name_plural = '4.Registrar Normas'
