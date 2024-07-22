import csv
from pathlib import Path

from django.shortcuts import render

PATH_TO_CSV = Path(__file__).parent.joinpath('data', 'feedback.csv')


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open(PATH_TO_CSV, 'a') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([name, phone, message])
    return render(request, 'catalog/contacts.html')
