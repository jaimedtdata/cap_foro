
import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.http import HttpResponse, HttpResponseRedirect

from apps.email import (send_confirm_account, send_success_sign_up,
    send_password_reset, send_success_password_reset,)

from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from apps.forms import (LiquidForm, SessionFormset, ComisionForm,PlanForm,CommentForm,
                             ArquitectFormset, EntrevistaFormset, EntrevistaForm, MUNI_CHOICES,
                             PROVINCE_CHOICES, RulesForm, UserLoginForm, ExternalRegisterForm)
from apps.choices import (AREAS_CHOICES, PUESTOS_CHOICES,
                               works_list, get_themes, SANCTIONS_CATEGORIES, PREVENTIONS_CHOICES,
                               SPECIALTIES_CHOICES)
from django.contrib.auth.views import (LoginView, LogoutView, 
    PasswordResetView, PasswordResetDoneView,)
from django.forms.models import model_to_dict
from apps.models import Plan, Policies_usage, Member, UserToken
from normas.models import Areas_Normas,Master_Normas,Categories_Normas
from foro.models import Coments_foro
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required




def get_rules(pk):
    #rpta_normas = Master_Normas.objects.all()
    rpta_normas = Master_Normas.objects.filter(area_name=pk)
    rules = []
    for i in rpta_normas:
            rules.append(
                {
                    'n': i.id,
                    'section': i.category_name,
                    'rule_type': i.subcategory_name,
                    'locations': i.location_name,
                    'norm': i.norma_rne,
                    'denom': i.norma_name,
                    'publication_date': i.validity_date_start,
                    'file':i.file,
                }
            )
    return rules

        
def dashboard(request):
    rpta_areas = Areas_Normas.objects.all()
    context = {'rpta_areas': rpta_areas}
    print (context)
    return render(request, 'dashboard.html', context)


def get_user_by_form_data(data, roles=[]):
        user = {
        'names': data['names'],
        'first_surname': data['first_surname'],
        'second_surname': data['second_surname'],
        'profession': data['profession'],
        'tuition': data['tuition'],
        'is_signature_validated': False,
        'mobile': data['mobile'],
        'email': data['email'],
        'roles': roles
        }
        return user

class SignUpOthers(CreateView):

    model = Member
    form_class = ExternalRegisterForm
    template_name = 'sign-up.html'
    #success_url = reverse_lazy('profiles:check_your_email')
    
    def form_valid(self, form):
        print('INGRESO A VALIDO!')
        


        profile = form.save(commit=False)

        group = Group.objects.get(name='Gratuito')      
        user = User.objects.create_user(profile.first_surname, profile.email, 'UEp8$x7rx@ZiSwU')
        user.last_name = profile.first_surname
        user.groups.add(group)
        user.save()


        #print('profile',profile)
        #registered_profile = Member.objects.filter(tuition=profile.tuition, profession=profile.profession)
        #if registered_profile:
        #    data = get_user_by_form_data(form.cleaned_data, ['PROP'])
        #    registered_profile.update(**data)
        token = UserToken(user_profile=profile)
        #else:
        profile.save()
        #profile.add_role(['PROP'])
        #profile.save()
            #token = UserToken(user_profile=profile)
        #token.save()
        #send_confirm_account(self.request, token.get_confirm_link(), profile.email)
        send_confirm_account(self.request, token.get_confirm_link(), profile.email)
        #return HttpResponseRedirect(reverse_lazy('profiles:check_your_email'))
        #return  reverse_lazy('dashboard:users')
        return HttpResponseRedirect(reverse_lazy('success_sign_up'))

    def form_invalid(self, form):
        print('INGRESO A INNVALIDO!',self,form)
        messages.error(self.request, 'Por favor, corrija los errores')
        return super(SignUpOthers, self).form_invalid(form)


def success_sign_up(request):
    messages.success(request, 'Registro Exitoso')
    return render(request, 'success_sign_up.html')	

def signup(request):
    return render(request, 'sign-up.html')

class Login(LoginView):
    authentication_form = UserLoginForm
    template_name = 'login.html'

    #def form_invalid(self, form):
    #    return super(Login, self).form_invalid(form)


#@login_required
def preguntas(request):
    cuestions = Policies_usage.objects.all()
    #cuestions = Policies_usage.objects.filter(pk=2)
    #for staff in cuestions:
    #    print (staff.norma_name.all())     
    context = {'cuestions': cuestions}
    return render(request, 'preguntas.html', context)
    

def password_reset(request):
    #cuestions = Policies_usage.objects.all()
    #cuestions = Policies_usage.objects.filter(pk=2)
    #for staff in cuestions:
    #    print (staff.norma_name.all())     
    context = {'cuestions': ''}
    return render(request, 'password_reset.html', context)



def preguntas_edit(request, pk=None):
    
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

def preguntas_delete(request, pk):
    print ('entro a borrar')
    plans = Plan.objects.get(id=pk)
    plans.delete()
    return redirect('/plan')

def checkout(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'checkout.html', context)

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

#def login(request):
#    return render(request, 'login.html')

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

@login_required
def rules(request):
   
    tipouso_id = request.GET.get('rule_id')
    print("request",tipouso_id)

    context = {
        'rules': True,
            'nonav': False,
            'categories': 'RULES_CATEGORIES',
            'sanctions': SANCTIONS_CATEGORIES,
            'preventions': PREVENTIONS_CHOICES,
            'filter': RulesForm(),
            'rules_list': get_rules(tipouso_id),
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
            'category_list': [],
            'themes': [],
    }
    return render(request, 'foro_temas.html', context)


def foro_comentarios(request):
    f_id = request.GET.get('rule_id')
    print ('ingreso Grabar!!')
    if request.method == "POST":
        comentario = request.POST.get('comentario')
        print ('POSTBOTON',comentario)
        b = Coments_foro(themas=f_id,user=request.user, coments=comentario)
        print ('POSTBBB',b)
        b.save()
        

    #print("request",f_id)
    
    normas = Master_Normas.objects.filter(id=f_id)
    comentarios = Coments_foro.objects.filter(user=1 ,themas=f_id)
    number_coments = comentarios.count()
    
    #data=model_to_dict(normas)  
    if not normas:
        context = {
            'foro': True,
                'denominacion':'',
                'ncomentarios': 0,
                'comentarios_list': [],
                'themes': [],
        }    
    else:
        context = {
            'foro': True,
                'denominacion':normas,
                'ncomentarios': number_coments,
                'comentarios_list': comentarios,
                'themes': [],
        }


    #comentarios_save(f_id)
    #context = {'data': normas}
    #print ('foro_datos',context)
    return render(request, 'foro_comentarios.html', context)

# def comentarios_save(request, pk=None):
    
#     post = get_object_or_404(Coments_foro, pk=pk)
   
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
            
#             #post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm(instance=post)
    

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


def member(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'member.html', context)


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


def get_foro_items():
    rpta_areas = Areas_Normas.objects.all()
    
    category_list = []
    title_list = {}
    detail_list = []
    item_list = []

    for a in rpta_areas:

        title_list['title']= a.area_name.title()
        
        rpta_normas = Master_Normas.objects.filter(area_name=a.id)
        nmessages=rpta_normas.count()
        for i in rpta_normas:
                
                item_list.append(
                        {
                        'title':i.norma_name.title(),
                        'themes_count': i.id,
                        'messages_count': nmessages,
                        'id': i.id,
                        },
                )
                
                dictionary_title_list= item_list.copy()
        title_list['items']=dictionary_title_list
        item_list = []
        print (dictionary_title_list)
        
        dictionary_copy = title_list.copy()
        
        detail_list.append(dictionary_copy)

    
    
    return detail_list

    # col_list = ['norma_name', 'id']
    # category_list.append(
    #     {
    #         'title': rpta_areas[1],
    #         'items': Master_Normas.objects.all().values_list(*col_list),
    #     },

    # )
    # category_list = (
    #     {
    #         'title': 'Temas Normativos',
    #         'items': [
    #             {
    #                 'title':'Licencias, Procedimientos Administrativos  para Licencias de Edificación',
    #                 'themes_count': random.randint(10,50),
    #                 'messages_count': random.randint(50,200),
    #             },
    #             {
    #                 'title':'Convenios',
    #                 'themes_count': random.randint(10,50),
    #                 'messages_count': random.randint(50,200),
    #                 'last_messages': (
    #                     {
    #                         'message':'Convenio Rimac Seguros',
    #                         'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
    #                     },
    #                     {
    #                         'message':'Convenio Clínica Ricardo Palma',
    #                         'date':'Ayer {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
    #                     },
    #                 )
    #             },				
    #         ],
    #     },
        
    # )
    # return category_list