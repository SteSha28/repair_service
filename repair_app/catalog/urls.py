from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.CatalogOptionPage.as_view(), name='catalog_option'),
    path('service_list/',
         views.ServiceListView.as_view(), name='service_list'),
]
