import csv
import os.path
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

PATH_TO_CSV = Path(__file__).parent.joinpath('data', 'feedback.csv')


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        is_csv_exists = os.path.exists(PATH_TO_CSV)
        with open(PATH_TO_CSV, 'a', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            if not is_csv_exists:
                csv_writer.writerow(['name', 'phone', 'message'])
            csv_writer.writerow([name, phone, message])
            # messages.success(request, 'Сообщение отправлено')
            return render(request, 'catalog/itsok.html')
    return render(request, 'catalog/contacts.html')
