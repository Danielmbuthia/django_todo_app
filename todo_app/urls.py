from django.urls import path

from .views import CustomLoginView, TodoCreateView, TodoDeleteView, TodoDetailView, TodoListView, TodoUpdateView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
    path('',TodoListView.as_view(), name='home'),
    path('detail/<pk>/',TodoDetailView.as_view(), name='detail'),
    path('edit/<pk>/',TodoUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='delete'),
    path('create/',TodoCreateView.as_view(),name='create')
]
