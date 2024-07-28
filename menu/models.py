from django.db import models


class Menu(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField('Описание', max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=300, blank=True, null=True)

    url = models.CharField('Адрес для перехода', max_length=50, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункты меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name