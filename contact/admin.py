from django.contrib import admin
from contact.models import Contact, Category


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show', 'owner',)
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 20
    list_max_show_all = 100
    list_editable = 'first_name', 'last_name', 'show'
    list_display_links = 'id', 'phone'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
