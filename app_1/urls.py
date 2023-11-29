from django.urls import path, include
from . import views


app_name = 'app_1'


urlpatterns = [
    path('page_1/', views.page_1, name='current'),
    path('page_2/', views.page_2, name='archive'),
    path('', views.main_page, name='main'),
]
 