from dataclasses import fields
from urllib import request, response
from django.http import HttpResponse, JsonResponse
from cadastroApp.models import Categoria, Fornecedor, Produto, Itens_Produto
from django.views import View
#from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
import json
#from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import status

    
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
    
class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ItensSerializer(ModelSerializer):
    class Meta:
        model = Itens_Produto
        fields = '__all__'
    
class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class ItensView(APIView):
    def get(self, request):
        itens = Itens_Produto.objects.all()
        serializer = ItensSerializer(itens, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItensSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItensDetail(APIView):
    
    def get(self, request, id):
        itens = get_object_or_404(Itens_Produto.objects.all(), id=id)
        serializer = ItensSerializer(itens)
        return Response(serializer.data)  

    def put(self, request, id):
        itens = get_object_or_404(Itens_Produto.objects.all(), id=id)
        serializer = ItensSerializer(itens, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        itens = get_object_or_404(Itens_Produto.objects.all(), id=id)
        itens.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriaView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetail(APIView):
    
    def get(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)  

    def put(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ProdutoView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdutoDetail(APIView):

    def get(self, request, id):
        produto = get_object_or_404(Produto.objects.all(), id=id)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)  

    def put(self, request, id):
        produto = get_object_or_404(Produto.objects.all(), id=id)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        produto = get_object_or_404(Produto.objects.all(), id=id)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            
              

class FornecedorView(APIView):

    def get(self, request):
        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FornecedorDetail(APIView):

    def get(self, request, id):
        fornecedor = get_object_or_404(Fornecedor.objects.all(), id=id)
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)  

    def put(self, request, id):
        fornecedor = get_object_or_404(Fornecedor.objects.all(), id=id)
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        fornecedor = get_object_or_404(Fornecedor.objects.all(), id=id)
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
