# steganography/views.py

from django.shortcuts import render
from django.views.generic.base import TemplateView

class BasePageView(TemplateView):
    template_name = 'steganography/base.html'