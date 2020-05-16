from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create', views.UserCreateAPIView.as_view(), name='create'),
    path('token', views.CreateTokenAPIView.as_view(), name='token'),
]
