#-*- coding: utf-8 -*-
from django import forms

class CalculForm(forms.Form):
    x = forms.IntegerField(label="x.",required=True)
    y = forms.IntegerField(label="y.",required=True)

class HelloForm(forms.Form):
    z = forms.CharField(label="z.",required=True)