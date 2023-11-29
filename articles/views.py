from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def special_case_2003(request):
    return HttpResponse('<h3>Articles 2003</h3>')

def year_archive(request, year):
    return HttpResponse(f'<h3>Archive Articles {year}</h3>') 

def month_archive(request, year, month):
    return HttpResponse(f'<h3>Archive Articles {year} year, {month} month</h3>')