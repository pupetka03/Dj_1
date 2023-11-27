from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_1_main(request):
    return render(request, 'app_1_main.html', context={'data': 'Hello, 1'})