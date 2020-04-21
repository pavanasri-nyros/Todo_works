from django.urls import path
from . import views

urlpatterns =[
    path('',views.home, name = 'home'),
    path('create/',views.createtodo, name = 'createtodo'),
    path('current/',views.currenttodos, name = "currenttodos"),
    path('completed/',views.completedtodos, name = "completedtodos"),
    path('todo/<int:todo_pk>',views.viewtodo, name = 'viewtodo'),
    path('todo/<int:todo_pk>/complete',views.completetodo, name = 'completetodo'),
    path('todo/<int:todo_pk>/delete',views.deletetodo, name = 'deletetodo'),
    
]