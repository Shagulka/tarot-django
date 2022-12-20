from django.contrib import admin

from .models import Fortune


@admin.register(Fortune)
class FortuneAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


