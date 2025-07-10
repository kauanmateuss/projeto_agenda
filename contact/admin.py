from django.contrib import admin
from .models import Contact, Category

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')  #Aqui trabalha com Tuplas
    ordering = ('id',)
    # list_filter = ('created_date',)   #Filtrando por data de criação

    #adicionando o campo de pesquisa
    search_fields = ('first_name', 'last_name', 'phone', 'email')

    # Definindo a quantidade de registros por página
    list_per_page = 20
    list_max_show_all = 100     # Mostra todos os registros

    # quais campos podem ser editados diretamente na lista
    list_editable = ('phone',)

    # Adicionando um link no campo nome
    list_display_links = ('id', 'first_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = '-id',