from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Producto
from .serializers import ClienteSerializer, ProductoSerializer
from rest_framework.permissions import AllowAny

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]