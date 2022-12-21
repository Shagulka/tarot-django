from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from coins.admin import BankAccountInline

from .forms import AccountChangeForm, AccountCreationForm
from .models import Account


@admin.register(Account)
class ProfileAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    inlines = (BankAccountInline,)

    list_display = ('email',
                    'first_name',
                    'last_name',
                    'is_staff',
                    'profile_picture')
    list_editable = ('is_staff',)
    ordering = ('email',)
    readonly_fields = ('password', 'date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {
            'fields': ('first_name',
                       'last_name',
                       'date_of_birth',
                       'profile_picture')
        }
        ),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',)}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2',),
        }),
    )
