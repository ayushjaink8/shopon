from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse("Hello World");

def home(request):
    return render(request, "test.html",{'name':'Naveen'});

def test2(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    val3 = val1 + val2
    return render(request, "test2.html", {'result': val3} );