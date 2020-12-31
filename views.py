from django.shortcuts import render
from Home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    # return render(request,'index.html')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Child = request.POST.get('Child')
        Phone = request.POST.get('Phone')
        contact = Contact(Name=Name, Child=Child, Phone=Phone, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message Has been sent successfully!')


    return render(request,'contact.html')