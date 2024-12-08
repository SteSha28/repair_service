from django.contrib import admin
from django.urls import path, include

handler404 = 'pages.views.page_not_found'

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('catalog/', include('catalog.urls')),
]
