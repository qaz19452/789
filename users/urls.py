from . import views
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path

app_name = 'users'
LoginView.template_name = 'users/login.html'
LogoutView.template_name = 'users/logout.html'
urlpatterns = (
    # 登录界面
    path('login/', LoginView.as_view(), name="login"),
    # 注销
    path('logout/', views.logout_view, name='logout'),
    # 注册界面
    path('register/', views.register, name='register'),


)
