from django.shortcuts import render
from django.views.generic import TemplateView
from tattoo.models import Tattoo

class HomeView(TemplateView):
    template_name = "index.html"
    
class PortofoliuView(TemplateView):
    template_name = "portofoliu.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tattoos'] = Tattoo.objects.all()
        return context
    
class GhidCompletView(TemplateView):
    template_name = "ghid_complet.html"
    
class IntrebariFreceventeView(TemplateView):
    template_name = "intrebari_frecvente.html"
    
class ContactView(TemplateView):
    template_name = "contact.html"
    
   