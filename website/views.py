from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello World");

def index(request):
    return render(request, "index.html");

def about(request):
    return render(request, "about.html");

def contact(request):
    return render(request, "contact.html");


def products(request):
    return render(request, "products.html");

def login_profile(request):
    return render(request, "index.html");






# def test2(request):
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     val3 = val1 + val2
#     return render(request, "test2.html", {'result': val3} );