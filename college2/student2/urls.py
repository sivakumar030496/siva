from django.urls import path
from .views import *

stu_urls=[
    path('home/',home),
    path('index/', index),
    path('register/', register),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
    path('login/', login),
    path('logout/', logout),
    path('send_mail/<str:email>', send_mail),

    #path('queries/', queriesql)
]