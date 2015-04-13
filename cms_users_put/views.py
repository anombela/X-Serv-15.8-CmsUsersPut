#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def cms_users_put(request, recurso):

    estado = ""
    if request.user.is_authenticated():
        estado += "</br>Eres " + request.user.username + "<a href='/logout'>Logout</a>"
    else:
        estado += "No estas autenticado. <a href='http://127.0.0.1:8000/admin/login/'>Haz login</a>"

    if request.method == 'GET':
        try:
            page = Pages.objects.get(name=recurso)
            return HttpResponse(page.page + estado)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("Page not found" + estado)

    elif request.method == 'PUT':
        if request.user.is_authenticated():
            newpage = Pages(name=recurso, page=request.body)
            newpage.save()
            return HttpResponse("Pagina guardada: " + request.body)
        else:
            return HttpResponse("No se puede añadir pagina " + estado)
    else:
        return HttpResponse("No esta disponible el metodo" + request.method)

    return HttpResponseNotFound( estado)