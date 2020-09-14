from django.urls import path
from Login import views

urlpatterns = [
    path('',views.index,name='index'),
]