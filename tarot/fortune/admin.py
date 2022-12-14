from django.contrib import admin

from .models import CardTitle, Fortune


@admin.register(Fortune)
class FortuneAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    filter_horizontal = ('title_for_cards',)


@admin.register(CardTitle)
class CardTitleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
