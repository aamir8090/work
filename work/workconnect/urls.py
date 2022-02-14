from django.urls import path
from . import views
urlpatterns = [
    path('', views.basehome, name='home'),
    path('contact', views.contact, name = 'contact'),
    path('aanmelden', views.aanmelden, name = 'aanmelden'),
    path('adduser', views.adduser, name = 'adduser'),
    path('overons', views.overons, name = 'overons'),
    path('login', views.login, name='login'),

]
