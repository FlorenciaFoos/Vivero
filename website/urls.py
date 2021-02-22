
from django.urls import path
from . import views
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contacto', views.contact, name='contact'),
    path('nosotros', views.nosotros, name='nosotros'),
    #filtro por categoria desde home
    
    #muestra el catalogo completo
    path('explorar', ProductosList.as_view(), name='explorar'),
    path('explorar/<int:category_id>/', ProductosFiltradosList.as_view(), name='explorar'),
]  +  static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

 