from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('completetodo/<todo_id>', views.completetodo, name='completetodo'),
    path('deletecompletedtodo', views.deletecompletedtodo, name='deletecompletedtodo'),
    path('deletealltodo', views.deletealltodo, name='deletealltodo')
]