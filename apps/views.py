
import random
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.forms import (LiquidForm, SessionFormset, ComisionForm,PlanForm,
                             ArquitectFormset, EntrevistaFormset, EntrevistaForm, MUNI_CHOICES,
                             PROVINCE_CHOICES, RulesForm,)
from apps.choices import (AREAS_CHOICES, PUESTOS_CHOICES,
                               works_list, get_rules, get_foro_items, get_themes, RULES_CATEGORIES, SANCTIONS_CATEGORIES, PREVENTIONS_CHOICES,
                               SPECIALTIES_CHOICES)

from django.forms.models import model_to_dict
from apps.models import User, Plan
from django.shortcuts import get_object_or_404


def preguntas(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'preguntas.html', context)


def plan_list(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'plan_list.html', context)


def carga_rules(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'carga_rules.html', context)


def plan(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'plan.html', context)

#https://elbauldelprogramador.com/crear-formularios-en-django-partir-de-un-modelo-con-modelform/
def plan_edit(request, pk=None):
    
    if request.method == "POST":
       form = PlanForm(request.POST) # Bound form
       post = form.save(commit=False)
       post.id=pk
       post.save()
       messages.success(request, 'Registro Guardado..!!')
       return redirect('/plan')

    else: 
        print('GET')
        if pk:
            plans = Plan.objects.get(id=pk)  
            data=model_to_dict(plans)  
            context ={'form': PlanForm(initial=data)}
            return render(request, 'plan_edit.html', context)
        else:
            form = PlanForm()
            context ={'form': form}
            return render(request, 'plan_edit.html',context)
         
def plan_delete(request, pk):
    print ('entro a borrar')
    plans = Plan.objects.get(id=pk)
    plans.delete()
    return redirect('/plan')


def login(request):
    return render(request, 'login.html')


def dash(request):
    context = {
        'dashboard': True,
    }
    return render(request, 'dash.html', context)


def works(request):
    context = {
        'works': True,
            'nonav': True,
            'places': MUNI_CHOICES[8:14],
            'areas': AREAS_CHOICES,
            'puestos': PUESTOS_CHOICES,
            'specialties': SPECIALTIES_CHOICES,
            'works_list': works_list,
    }
    if request.method == 'POST':
        context['alert'] = 'Registros Filtrados'
    return render(request, 'works.html', context)


def rules(request):
    context = {
        'rules': True,
            'nonav': False,
            'categories': RULES_CATEGORIES,
            'sanctions': SANCTIONS_CATEGORIES,
            'preventions': PREVENTIONS_CHOICES,
            'filter': RulesForm(),
            'rules_list': get_rules(),
    }
    if request.method == 'POST':
        context['alert'] = 'Registros Filtrados'
    return render(request, 'rules.html', context)


def foro(request):
    context = {
        'foro': True,
            'category_list': get_foro_items(),
            'themes': get_themes(),
    }
    return render(request, 'foro.html', context)


def foro_temas(request):
    context = {
        'foro': True,
            'category_list': get_foro_items(),
            'themes': get_themes(),
    }
    return render(request, 'foro_temas.html', context)


def foro_comentarios(request):
    context = {
        'foro': True,
            'category_list': get_foro_items(),
            'themes': get_themes(),
    }
    return render(request, 'foro_comentarios.html', context)


def index(request):
    context = {
        'dashboard': True,
            'munis': MUNI_CHOICES[1:11],
            'provs': PROVINCE_CHOICES,
            'cantidades': [random.randrange(1, 10000) for i in range(100)],
    }
    return render(request, 'dashboard.html', context)


def charts(request):
    context = {
        'charts': True,
    }
    return render(request, 'charts.html', context)

# def users(request):
# 	context = {
# 		'users':True,
# 	}
# 	return render(request, 'users.html', context)


def member(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'member.html', context)


def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)


def users_create(request):
    return render(request, 'users_create.html')


def users_save(request):

    users = User(firstname=request.POST['firstname'], lastname=request.POST['lastname'] , document = 'NULL')
    users.save()
    return redirect('/users')


def users_edit(request, id):
    users = User.objects.get(id=id)
    context = {'users': users}
    return render(request, 'users_edit.html', context)


def users_update(request, id):
    users = User.objects.get(id=id)

    users.firstname = request.POST['firstname']
    users.lastname = request.POST['lastname']
    users.document = request.POST['lastname']
    users.save()
    return redirect('/users')


def users_delete(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect('/users')


def configs(request):
    context = {
            'config': True,
    }
    return render(request, 'config.html', context)


def liquid(request):
    context = {
            'liquid': True,
            'form': LiquidForm(),
            'formset': SessionFormset(prefix='sessions'),
    }
    return render(request, 'liquid.html', context)


def comision(request):
    context = {
            'comision': True,
            'form': ComisionForm(),
            'formset': ArquitectFormset(),
    }
    return render(request, 'comision.html', context)


def entrevistas(request):
    context = {
            'entrevistas': True,
            'form': EntrevistaForm(),
            'formset': EntrevistaFormset(),
    }
    return render(request, 'entrevistas.html', context)
