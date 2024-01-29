
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register,name="register_page"),
    path('login/', views.user_login,name="user_login"),
    path('profile/', views.profile,name="profile_page"),
    path('logout/', views.user_logout,name="user_logout"),
    path('pass_change/', views.password_change,name="pass_change"),
    path('pass_change_without_old_pass/', views.password_change2,name="pass_change_without_old_pass"),
]
