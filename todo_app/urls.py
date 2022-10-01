from django.urls import path

from .views import TodoCreateView, TodoDeleteView, TodoDetailView, TodoListView, TodoUpdateView

urlpatterns = [
    path('',TodoListView.as_view(), name='home'),
    path('detail/<pk>/',TodoDetailView.as_view(), name='detail'),
     path('edit/<pk>/',TodoUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='delete'),
    path('create/',TodoCreateView.as_view(),name='create')
]
