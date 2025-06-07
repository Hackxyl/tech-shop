from django.shortcuts import render,redirect
from django.contrib import messages
from .models import product,contactMessage
from django.core.mail import send_mail as send_email
# Create your views here.
def home(request):
   
    return render(request, 'home/home.html')

def products(request):
    products = product.objects.all()

    context = {
        'products': products,
    } 
    return render(request, 'home/products.html', context)



def contact(request):
    if request.method == "POST":

        # handle form submission here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # send email to site owner
        send_email(
            subject=f"New contact message from {name}",
            message=message,
            from_email=email,
            recipient_list=['hackxyl58@gmail.com'],
        )
        messages.success(request, "Thank you for contacting us!")
        return redirect('contact')
    # Always return a response for GET or other methods
    return render(request, 'home/contact.html')


    

def about(request):
    return render(request, 'home/about.html')


