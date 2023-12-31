"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_1.views import app_1_main
from app_2.views import app_2_main
from app_3.views import app_3_main
import articles.views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('articles/2003/', articles_views.special_case_2003),
    path('articles/<int:year>/', articles_views.year_archive),
    path('articles/<int:year>/<int:month>/', articles_views.month_archive),


    path('app_1/', include('app_1.urls')),
    path('app_2/', app_2_main),
    path('app_3/', app_3_main),
    path('', app_1_main),
]
