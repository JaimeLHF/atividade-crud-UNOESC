from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy 
from .models import Funcionarios

# Create your views here.

class FuncionarioCreateView(CreateView):
    model = Funcionarios
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios") 

class FuncionarioListView(ListView):
    model = Funcionarios
    template_name = "lista_funcionarios.html"

class FuncionarioUpdateView(UpdateView):
    model = Funcionarios
    fields = ("nome", "data_nascimento", "email", "profissao")
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios") 

class FuncionarioDetailView(DetailView):
    model = Funcionarios
    template_name = "lista_funcionario.html"
    context_object_name = "fun"

class FuncionarioDeleteView(DeleteView):
    model = Funcionarios
    template_name = "remover_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios") 