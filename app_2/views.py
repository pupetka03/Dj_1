from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_2_main(request):
    return render(request, 'app_2_main.html', context={'data': 'Hello, 2'})
