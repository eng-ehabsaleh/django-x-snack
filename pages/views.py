from django.views.generic import (ListView,CreateView,UpdateView,DeleteView,DetailView)

from .models import Snack
class HomePageView(ListView):
    template_name = 'pages/home.html'


# class AboutPageView(TemplateView):
#     template_name = 'pages/about.html'


from django.db import models
from django.shortcuts import render
from .models import Snack
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

# Create your views here.


class SnackListView(ListView):
    template_name = "pages/snack_list.html"
    model = Snack
    context_object_name = 'snack_list'


class SnackDetailView(DetailView):
    
    template_name = "pages/snack_detail.html"
    model = Snack



class SnackCreateView(CreateView):
    template_name = "pages/snack_create.html"
    model = Snack
    fields = ["title", "description", "purchaser"]
    context_object_name = "snack_create"



class SnackUpdateView(UpdateView):
    template_name = "pages/snack_update.html"
    model = Snack
    fields = ["title", "description", "purchaser"]
    context_object_name = "snack_update"


class SnackDeleteView(DeleteView):
    template_name = "pages/snack_delete.html"
    model=Snack
    success_url = reverse_lazy('snack_list')
    context_object_name = "snack_delete"