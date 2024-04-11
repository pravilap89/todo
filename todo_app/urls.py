
from django.contrib import admin
from django.urls import path
from . import views

app_name='todo_app'
urlpatterns = [
    path('', views.home,name='home'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('listview/',views.TaskListView.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.TaskDetailView.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.TaskUpdateView.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.TaskDeleteView.as_view(),name='deleteview'),
]
