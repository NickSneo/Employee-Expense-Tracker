from django.contrib import admin
from django.urls import path
from Register.views import loginUser, home, logoutUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('loginUser/', loginUser, name="loginUser"),
    path('logoutUser/', logoutUser, name="logoutUser"),
    # path('register/', register, name="register"),
    # path('viewExpenses/', viewExpenses, name="viewExpenses"),

]
