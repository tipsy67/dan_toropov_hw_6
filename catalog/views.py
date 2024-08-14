import csv
import os.path
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from catalog.models import Product, Contact, Feedback

PATH_TO_CSV = Path(__file__).parent.joinpath('data', 'feedback.csv')


# Create your views here.
def index(request):
    print(Product.objects.all().order_by('-created_at')[:5])
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Feedback.objects.create(name=name, phone=phone, message=message)
        return render(request, 'catalog/itsok.html')
    data = Contact.objects.all()[:1]
    if data:
        data = data[0]
    return render(request, 'catalog/contacts.html', context={'data': data})
