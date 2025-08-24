from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Oficina
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class OficinaListView(ListView):
    model = Oficina
    template_name = "oficina/lista.html"
    context_object_name = "oficinas"

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['titulo'] = 'Lista de Oficinas'
    #    return context