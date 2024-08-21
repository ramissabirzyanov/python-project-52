from django.urls import path
from task_manager.user import views

urlpatterns = [
    path('', views.UsersIndexView.as_view(), name='users'),
    # path('<int:id>/edit/', views.UserFormEditView.as_view(), name='article_update'),
    # path('<int:id>/delete/', views.UserFormDeleteView.as_view(), name='articles_delete'),
    # path('<int:id>/', views.UserView.as_view(), name='article_id'),
    # path('create/', views.UserCreateView.as_view(), name='article_create'),
]