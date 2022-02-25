from django.urls import path
from . import views

urlpatterns = [
    path('web', views.web, name='web'),
    path('adver', views.adver, name='adver'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<int:id>/', views.update, name='update')

]
