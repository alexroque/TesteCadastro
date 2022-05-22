from django.contrib import admin
from django.urls import path
from cadastroApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', views.CategoriaView.as_view()),
    path('categoriasdetail/<int:id>/', views.CategoriaDetail.as_view()),
    path('fornecedores/', views.FornecedorView.as_view()),
    path('fornecedoresdetail/<int:id>/', views.FornecedorDetail.as_view()),
    path('produtos/', views.ProdutoView.as_view()),
    path('produtosdetail/<int:id>/', views.ProdutoDetail.as_view()),
    path('itens/', views.ItensView.as_view()),
    path('itensdetail/<int:id>/', views.ItensDetail.as_view()),
]
