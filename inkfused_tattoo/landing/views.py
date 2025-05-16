from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"
    
class PortofoliuView(TemplateView):
    template_name = "portofoliu.html"
    
class GhidCompletView(TemplateView):
    template_name = "ghid_complet.html"
    
class IntrebariFreceventeView(TemplateView):
    template_name = "intrebari_frecvente.html"
    
class ContactView(TemplateView):
    template_name = "contact.html"