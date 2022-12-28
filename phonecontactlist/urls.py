from django.contrib import admin
from django.urls import path, include
from phonecontactlist.views import add_contact,delete_contact,single_view_contact,index

urlpatterns = [
    path('add_contact/', add_contact, name = 'add_contact'),
    path('index/', index, name = 'index'),
    # path('view_all_contact/', view_all_contact, name = 'view_all_contact'),
    path('delete_contact/', delete_contact, name = 'delete_contact'),
    path('view_contact/', single_view_contact, name = 'single_view_contact'),
   
]