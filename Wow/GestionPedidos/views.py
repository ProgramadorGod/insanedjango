from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articles
from django.core.mail import EmailMessage
from django.core.mail import send_mail
# Create your views here.

def search_products(request):
    return render(request, 'products_search.html')

def searching(request):
    if request.GET['prdt']:
        message = 'Article searched: %r' %request.GET['prdt']
        product = request.GET['prdt']
        if len(product)>20:
            message = 'The message is too long, try again'
        else:
            articles = Articles.objects.filter(name__icontains=product)
            return render(request, 'SearchResults.html', {'articles':articles, 'query':product})
    else:
        message = "You didnt introduced any value"
    
    
    return HttpResponse(message)


def contact(request):
    if request.method == 'POST':
        email = EmailMessage(
            'message1',
            'message2',
            'd2b854bb60cbed@inbox.mailtrap.io',
            ['d2b854bb60cbed@inbox.mailtrap.io']
        )
        email.send()

        return render(request, 'thanks.html')
    
    return render(request, 'contact.html')