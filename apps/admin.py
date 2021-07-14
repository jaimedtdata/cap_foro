from django.contrib import admin
from django.apps import apps
from .models import (Categories_Normas,)


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)

# Register your models here.
class MunicipalitiesAdmin(admin.ModelAdmin):
	list_display =['category_name']
	list_filter = ['category_name']
	search_fields = ['category_name']

admin.site.register(Categories_Normas, MunicipalitiesAdmin)

models = apps.get_models()


for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass




# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass