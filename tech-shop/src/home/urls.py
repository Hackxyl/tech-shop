from django.urls import path
from home.views import home,products,contact,about

urlpatterns = [
    path('', home, name='home'),
    
    path('products/', products, name='products'),

    path('contact/', contact, name='contact'),

    path('about/', about, name='about'),
]