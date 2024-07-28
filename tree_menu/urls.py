from django.contrib import admin
from django.urls import path

from menu.views import index, draw_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main_menu'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
