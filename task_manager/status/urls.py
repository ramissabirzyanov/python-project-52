from django.urls import path
from task_manager.status import views

urlpatterns = [
    path('', views.StatusListView.as_view(), name='statuses'),
    path('create/', views.StatusCreateView.as_view(), name='status_create'),
]