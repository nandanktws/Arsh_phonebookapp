"""Phonelist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from phonecontactlist.urls import path
from phonecontactlist.views import add_contact,delete_contact,single_view_contact,index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_contact/', add_contact, name = 'add_contact'),
    # path('view_all_contact/', view_all_contact, name = 'view_all_contact'),
    path('delete_contact/', delete_contact, name = 'delete_contact'),
    path('view_contact/', single_view_contact, name = 'single_view_contact'),
    path('index/', index, name = 'index'),
    
    

]
