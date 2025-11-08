from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/', views.UserList.as_view(), name='user_list'),
    path('api/v1/users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]
