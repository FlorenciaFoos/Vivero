
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto', views.contact, name='contact'),
    path('nosotros', views.nosotros, name='nosotros'),
    #filtro por categoria desde home
    path('<int:CategoriaId>/', views.categoria, name='categoria'),
    #muestra el catalogo completo
    path('explorar', ProductosList.as_view(), name='explorar'),
]
