from django.contrib import admin
from .models import usuarios
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.

# @admin.register(get_user_model())
# class CustomUserAdmin(UserAdmin):
#     pass



class UserAdmin(UserAdmin):
    fieldsets = (
        ('Credenciales', {'fields': ('username','password','email')}),
        ('Información personal', {"fields": ('first_name','address',)}),
        ('Permisos', {"fields": ('is_active','tipo_usuario')}),

    )
    ## datos que se muestran en el panel de django admin
    #list_display= ('email','username','tipo_usuario')

admin.site.register(usuarios,UserAdmin)

