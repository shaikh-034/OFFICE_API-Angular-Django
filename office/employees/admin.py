from django.contrib import admin
from employees.models import Employees_data, EmployeePersonalInfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
class EmployeeModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'tc', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Employee Credential', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('tc',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. EmployeeModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'tc', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('id','email',)
    filter_horizontal = ()


# Now register the new EmployeeModelAdmin...
admin.site.register(Employees_data, EmployeeModelAdmin)
admin.site.register(EmployeePersonalInfo)


