# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




# Create your views here.

def text(request):
  text = """<h1>Première page</h1>"""
  return HttpResponse(text)
  
def home(request):
    from Algo.Run import run
    temp=run()
    solution=temp[0]
    solution_tab=temp[1]
    return render(request, 'application/home.html',locals())


