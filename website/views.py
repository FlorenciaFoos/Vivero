from django.shortcuts import render
from django.core.mail import send_mail

##paso la peticion, template, contexto
def home(request):
    return render(request, 'home.html', {})

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
         return render(request, 'contact.html', {'message_name': message_name})
    else:    
        return render(request, 'contact.html', {})


def nosotros(request):
    return render(request, 'nosotros.html', {})