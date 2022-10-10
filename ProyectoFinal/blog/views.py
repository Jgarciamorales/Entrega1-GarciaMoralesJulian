from django.shortcuts import render
from blog.forms import formAutor, formArticulo, formSeccion
from blog.models import *

# Create your views here.


def inicio(request):

    return render(request, "blog/padre.html")


def articulo(request):

    return render(request, "blog/articulo.html")


def autor(request):

    return render(request, "blog/autor.html")


def seccion(request):

    return render(request, "blog/seccion.html")


def cargarArticulo(request):
    if request.method == "POST":

        miFormulario = formArticulo(request.POST)  # aqui me llega la info del html
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            articulo = Articulo(
                titulo=informacion["titulo"], texto=informacion["texto"]
            )

            articulo.save()

            return render(request, "blog/inicio.html")

    else:

        miFormulario = formAutor()

    return render(request, "blog/cargarArticulo.html", {"miFormulario": miFormulario})


def cargarAutor(request):
    if request.method == "POST":

        miFormulario = formAutor(request.POST)  # aqui me llega la info del html
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            autor = Autor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                profesion=informacion["profesion"],
            )

            autor.save()

            return render(request, "blog/inicio.html")

    else:

        miFormulario = formAutor()

    return render(request, "blog/cargarAutor.html", {"miFormulario": miFormulario})


def cargarSeccion(request):
    if request.method == "POST":

        miFormulario = formSeccion(request.POST)  # aqui me llega la info del html
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            seccion = Seccion(nombre=informacion["nombre"])

            seccion.save()

            return render(request, "blog/inicio.html")

    else:

        miFormulario = formAutor()

    return render(request, "blog/cargarSeccion.html", {"miFormulario": miFormulario})
