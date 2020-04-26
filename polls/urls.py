from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.login, name='login'),
    path('pickle', views.pickle, name = 'pickle'),
    path('newItem', views.newItem, name = 'newItem'),
    path('calculateHappiness', views.calculateHappiness, name='calculateHappiness'),
    path('validateLogin', views.validateLogin, name='validateLogin'),
    path('dataEntry', views.dataEntry, name='dataEntry'),
    path('bubbles', views.bubbles, name='bubbles'),
    path('shapes', views.shapes, name='shapes'),
    path('semantic', views.semantic, name='semantic')
    
]