from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('signup/',views.signupform,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('todo/',views.todo,name='todo'),

    path('todo_completed/',views.completed,name='todo_completed'),


    path('signout/',views.signout,name='signout'),
    

    path("delete/<int:id>",views.delete,name='delete'),
    path("modify/<int:id>",views.modify,name='modify'),
]
