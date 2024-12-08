from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Service, Component


class CatalogOptionPage(TemplateView):
    """Класс, генерирующий главную страницу."""

    template_name = 'catalog/catalog_option.html'


class ServiceListView(ListView):
    """Список услуг."""

    model = Service
    ordering = '-price'
    paginate_by = 2