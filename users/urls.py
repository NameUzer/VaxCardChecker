from django.urls import path
from django.conf import settings
from .import views
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('',views.index, name='index'),
    path('Register',views.Register, name='Register'),
    path('processRegister',views.processRegister, name="processRegister"),
    path('infos',views.infos, name='infos'),
    path('search',views.search, name='Search'),
    path('index',views.index, name='Home'),
    path('terms', views.terms, name='terms'),
    path('WaitingArea',views.WaitingArea, name='WaitingArea'),
    path('StillInProcess',views.StillInProcess, name='StillInProcess'),
    path('About',views.About, name='About')]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)