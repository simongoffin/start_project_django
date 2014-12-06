# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from application.forms import CalculForm
import json




# Create your views here.

def home(request):
    from Algo.Run import run
    check=False
    error=False
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CalculForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            z=run(x,y)
            check=True
        else:
            message="Bad value"
            error=True
        return render(request, 'application/home.html',locals())
    else:
        form = CalculForm()
        return render(request, 'application/home.html',locals())

def hello(request):
    response_data = {}
    response_data['message'] = 'Hello World'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
        
