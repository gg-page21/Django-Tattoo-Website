
from django.urls import path
from .views import HomeView, PortofoliuView, GhidCompletView, IntrebariFreceventeView, ContactView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portofoliu/', PortofoliuView.as_view(), name='portofoliu'),
    path('ghid-complet/', GhidCompletView.as_view(), name='ghid_complet'),
    path('intrebari-frecvente/', IntrebariFreceventeView.as_view(), name='intrebari_frecvente'),
    path('contact/', ContactView.as_view(), name='contact'),

]