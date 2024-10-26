from django.urls import path
from . import views
urlpatterns = [
    path('', views.todo ,name='todo'),
    path('delete/<int:todo_id>', views.removetask ,name='delete'),
]
