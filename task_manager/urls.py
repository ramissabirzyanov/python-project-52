from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main page'),
    path('users/', include('task_manager.user.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
]
