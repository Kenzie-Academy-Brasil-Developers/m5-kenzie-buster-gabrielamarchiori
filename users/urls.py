from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('users/<int:user_id>/', views.UserDetailView.as_view())
]
