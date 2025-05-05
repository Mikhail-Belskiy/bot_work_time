from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': ['Главная','Вход','Регистрация','Отчёт']
    }
    return render(request,'app/index.html', data )