from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .models import Contact_list
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    contactlist = Contact_list.objects.all()
    print( Contact_list.objects.all())
    context = {'contactlist': contactlist}
    return render(request, 'view_phonebook.html', context)


def add_contact(request):
    name = request.POST.get('name')
    contact_number = request.POST.get('contact_number')
    list = Contact_list(name=name, contact_number=contact_number)
    list.save()
    return render(request, 'add.html')

def add_contact(request):   
    if request.method == 'POST':
        
        new_contact = Contact_list(
            Name= request.POST['Name'],
            Contact_number = request.POST['Contact_number'],
            
        )
        print("@@@@@@") 
        new_contact.save()
        return redirect('add_contact/')

    return render(request, 'phone_book.html')

def delete_contact(request):
     return HttpResponse("delete single contact")

def single_view_contact(request):
     return HttpResponse("deletea all contact") 
    

def single_view_contact(request):
     return HttpResponse("single view contact") 