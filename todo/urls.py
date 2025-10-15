from django.urls import path
from . import views

urlpatterns = [
    path('', views.List_todo, name='list_todo'),                # List all todos
    path('create/', views.create_todo, name='create_todo'),     # Create new todo
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),  # Delete a todo
    path('update/<int:pk>/', views.update_todo, name='update_todo'),  # Update a todo
]
