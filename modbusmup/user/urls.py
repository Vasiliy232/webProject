from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginUserApiView.as_view(), name='login_user'),
    path('logout/', views.LogoutUserApiView.as_view(), name='logout_user')
]
