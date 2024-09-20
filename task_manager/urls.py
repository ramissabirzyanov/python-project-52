from django.contrib import admin
from django.urls import path, include
from task_manager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main_page'),
    path('users/', include('task_manager.user.urls'), name='users'),
    path('statuses/', include('task_manager.status.urls'), name='statuses'),
    path('tasks/', include('task_manager.task.urls'), name='tasks'),
    path('labels/', include('task_manager.label.urls'), name='labels'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
