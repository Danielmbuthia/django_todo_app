from django.urls import path

from .views import TodoDeleteView, TodoListView

urlpatterns = [
    path('',TodoListView.as_view(), name='home'),
    path('delete/<int:pk>',TodoDeleteView.as_view(),name='delete')
]
