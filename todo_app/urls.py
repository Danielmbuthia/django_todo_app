from django.urls import path

from todo_app.views import delete, home

urlpatterns = [
    path('',home, name='home'),
    path('delete/<int:id>',delete,name='delete')
]
