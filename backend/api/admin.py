from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from api.models import *
 
# Register your models here.

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =['username', 'id', 'name', 'role', 'staff' , 'superuser', 'password']

@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =[field.name for field in Role._meta.fields]

@admin.register(Permission)
class PermissionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =[field.name for field in Permission._meta.fields]

@admin.register(Document)
class DocumentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =[field.name for field in Document._meta.fields]
    
@admin.register(Logs)
class LogsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =[field.name for field in Logs._meta.fields]