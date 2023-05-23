from.import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('result/',views.result,name='result'),
    path('address/',views.address,name='address'),
    path('contact/', views.contact, name='contact'),
    path('destinations/', views.destinations, name='destinations'),
    path('elements/', views.elements, name='elements'),
    path('news/', views.news, name='news'),

]