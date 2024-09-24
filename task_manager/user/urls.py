from django.urls import path
from task_manager.user import views

urlpatterns = [
    path('',
         views.UsersListView.as_view(),
         name='users'),
    path('<int:pk>/update/',
         views.UserUpdateView.as_view(),
         name='user_update'),
    path('<int:pk>/delete/',
         views.UserDeleteView.as_view(),
         name='user_delete'),
    path('create/',
         views.UserCreateView.as_view(),
         name='user_create'),
]
