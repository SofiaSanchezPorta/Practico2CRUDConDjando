from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Oficina
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

class OficinaListView(ListView):
    model = Oficina
    template_name = "oficina/lista.html"
    context_object_name = "oficinas"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Oficinas'
        return context
    
class OficinaDetailView(DetailView):
    model = Oficina
    template_name = "oficina/detalle.html"
    context_object_name = "oficinas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        oficina = self.object
        context["personas"] = oficina.personas.all().order_by("apellido")
        return context

class OficinaCreateView(LoginRequiredMixin, CreateView):
    model = Oficina
    template_name = "oficina/crear.html"
    fields = ['nombre', 'nombre_corto']
    success_url = reverse_lazy('oficina:lista')
    context_object_name = "oficina" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear oficina'
        return context
    
class OficinaUpdateView(LoginRequiredMixin, UpdateView):
    model = Oficina
    template_name = "oficina/crear.html"
    fields = ['nombre','nombre_corto']
    success_url = reverse_lazy('oficina:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar oficina'
        return context
    
class OficinaDeleteView(LoginRequiredMixin, DeleteView):
    model = Oficina
    template_name = "oficina/eliminar.html"
    context_object_name = "oficina"
    success_url = reverse_lazy('oficina:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'eliminar'
        context['title'] = 'Eliminar oficina'
        return context
    
class OficinaSearchView(ListView):
    model = Oficina
    template_name = "oficina/buscar.html"
    context_object_name = "oficinas"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Oficina.objects.filter(
                Q(nombre__icontains=query) | Q(nombre_corto__icontains=query)
                )
        return Oficina.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Búsqueda de oficinas'
        context['query'] = self.request.GET.get("q", "")

        return context