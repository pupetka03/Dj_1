from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def app_1_main(request):
    return render(request, 'app_1_main.html', context={'data': 'Hello, 1'})

def page_1(request):
    return render(request, 'app_1_main.html', context={'data': 'page 1 app 1'})

def page_2(request):
    return redirect('app_1:main')

def main_page(request):
    return render(request, 'app_1_main.html', context={'data': 'main page app 1'})

