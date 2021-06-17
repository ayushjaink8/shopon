from django.urls import path, include

from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('products/',views.products, name='products'),
    path('accounts/profile/',views.products, name='login_profile'),
]