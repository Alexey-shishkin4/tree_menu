from django.shortcuts import render

from menu.models import Menu


def index(request):
    return render(request, 'index.html', {'menu': Menu.objects.all()})


def draw_menu(request, path):
    path = path.split('/')
    assert len(path) > 0, ('= Draw_menu function failed =')
    return render(request, 'index.html', {
        'menu_name': path[0],
        'menu_item': path[-1]
    })