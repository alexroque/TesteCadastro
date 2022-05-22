from django.contrib import admin

from cadastroApp.models import Categoria, Fornecedor, Itens_Produto, Produto

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Itens_Produto)


 
