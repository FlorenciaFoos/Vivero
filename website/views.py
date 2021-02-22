from django.shortcuts import render
from django.core.mail import send_mail
from .models import Producto, Categoria
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView 



class Home(ListView): 
    #para la vista 'home'
    model = Categoria 
    template_name = 'website/home.html'


def contact(request):
    if request.method == 'POST':
         message_name = request.POST['name']
         message_email = request.POST['email']
         message = request.POST['message']
         category = request.POST['category']
      
         #send email - params: subject, message, from email, to email
         send_mail(
            category + '/' + message_email ,
            message,
       
            message_email,
            ['florenciafoos212@gmail.com'],
            fail_silently = True
         )
         return render(request, 'website/contact.html', {'message_name': message_name})
    else:    
        return render(request, 'website/contact.html', {})


def nosotros(request):
    return render(request, 'website/nosotros.html', {})



 
 


class ProductosList(ListView): 
    #para la vista 'explorar/id'
    #template = producto_list.html
    model = Producto 
    template_name = 'website/producto_list.html'

 
class ProductosFiltradosList(ListView): 
    #para la vista 'explorar/id'
    #template = producto_list.html
    model = Producto 
    template_name = 'website/producto_list.html'
    def get_queryset(self):
        return Producto.objects.filter(ProductoCategoria=self.kwargs['category_id'])
