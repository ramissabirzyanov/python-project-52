from django.contrib import admin
from django.urls import path, include
from task_manager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main_page'),
    path('users/', include('task_manager.user.urls'), name='users'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
