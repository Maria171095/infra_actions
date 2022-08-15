from django.http import HttpResponse


def index(request):
    return HttpResponse('Получилось один, получится и второй раз!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
