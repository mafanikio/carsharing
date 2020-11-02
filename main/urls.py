from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:id>', views.index, name='index'),
    path('view/', views.view, name='view'),
    path('service/', views.service, name='service'),
    path('cars/', views.cars, name='cars'),
    path('workers/', views.workers, name='workers'),
    path('orders/', views.orders, name='orders'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
