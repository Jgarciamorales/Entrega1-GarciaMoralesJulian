"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import (
    inicio,
    autor,
    articulo,
    seccion,
    cargarArticulo,
    cargarAutor,
    cargarSeccion,
    buscar,
    busqueda,
)

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("autor/", autor, name="autor"),
    path("articulo/", articulo, name="articulo"),
    path("seccion/", seccion, name="seccion"),
    path("cargarAutor/", cargarAutor, name="cargarAutor"),
    path("cargarArticulo/", cargarArticulo, name="cargarArticulo"),
    path("cargarSeccion/", cargarSeccion, name="cargarSeccion"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
]
