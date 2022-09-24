from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, reverse
import os
import datetime, pytz


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d-%m-%Y %H:%M:%S")   
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    path = '.'
    msg = os.listdir(path)
    print(msg)
    return JsonResponse(msg, safe = False)