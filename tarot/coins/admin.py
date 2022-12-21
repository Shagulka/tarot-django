from django.contrib import admin

from .models import BankAccount


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'bonus')
    list_editable = ('balance',)
    ordering = ('user',)
    readonly_fields = ('user', 'bonus')


admin.site.register(BankAccount, BankAccountAdmin)


class BankAccountInline(admin.StackedInline):
    model = BankAccount
    extra = 0
    can_delete = False
    readonly_fields = ('balance', 'bonus')
