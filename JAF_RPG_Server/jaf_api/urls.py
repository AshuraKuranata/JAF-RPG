from django.urls import path
from . import views
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('api/v1/users/', views.UserList.as_view(), name='user_list'),
    path('api/v1/users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    
    # FOR JWT AUTHENTICATION
    path('sample/', views.SampleView.as_view(),name='sample'),
    path('api/token/', TokenObtainPairView.as_view(),
          name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
          name='token_refresh'),
]
