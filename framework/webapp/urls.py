from django.urls import path
from .views import *

urlpatterns=[
    path('details/',details),
    path('create/',create),
    path('delete/<int:id>/',delete1),
    path('update/<int:id>/',update)
]