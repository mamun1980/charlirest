from django.contrib import admin
from django.apps import apps

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    list_display = [field.name for field in Author._meta.get_fields()]

admin.site.register(Author, AuthorAdmin)


admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Movie)





# all_models = apps.get_app_config('posts').get_models()
#
# for model in all_models:
#     admin.site.register(model)
