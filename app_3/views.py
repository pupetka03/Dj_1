from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_3_main(request):
    return render(request, 'app_3_main.html', context={'data': 'Hello, 3'})