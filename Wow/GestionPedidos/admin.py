from django.contrib import admin

# Register your models here.

from GestionPedidos.models import Clients, Articles, Tasks

class ClientsAdmin(admin.ModelAdmin):
    list_display=("name", "address", "phone")
    search_fields=('name', 'phone')

class ArticlesAdmin(admin.ModelAdmin):
    list_filter=('section',)

class TasksAdmin(admin.ModelAdmin):
    list_display=("number", "date", "delivered")
    list_filter=('date',)
    date_hierarchy='date'

admin.site.register(Clients, ClientsAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Tasks, TasksAdmin)