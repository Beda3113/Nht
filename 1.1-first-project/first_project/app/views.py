from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
   
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'), 
        'Показать содержимое рабочей директории': reverse('workdir'),  
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    # Получаем текущее время
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
   
    files = os.listdir('.')  # '.' 
    msg = 'Содержимое рабочей директории:<br>' + '<br>'.join(files)
    return HttpResponse(msg)
