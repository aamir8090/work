from django.urls import path
from . import views
urlpatterns = [
    path('', views.basehome, name='home'),
    path('contact', views.contact, name = 'contact'),
    path('aanmelden', views.aanmelden, name = 'aanmelden'),
    path('adduser', views.adduser, name = 'adduser'),
    path('overons', views.overons, name = 'overons'),
    path('login', views.login, name='login'),
    path('form', views.form),
    path('business', views.business, name='business'),
    path('index', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('create', views.create, name='create'),
    path('page', views.page, name='page'),

]
