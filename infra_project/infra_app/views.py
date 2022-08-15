from django.http import HttpResponse


def index(request):
    return HttpResponse('Получилось второй раз!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
