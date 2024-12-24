from django.urls import path
from myapp import views
urlpatterns = [

path('Form/', views.mark_form, name='mark_form'),
path('List/', views.mark_list, name='mark_list'),

]