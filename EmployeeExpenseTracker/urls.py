from django.contrib import admin
from django.urls import path
from Register.views import loginUser, home, logoutUser, inputExpense, registerEmp
from ViewExpenses.views import viewExpenses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('loginUser/', loginUser, name="loginUser"),
    path('logoutUser/', logoutUser, name="logoutUser"),
    path('registerEmp/', registerEmp, name="registerEmp"),
    path('inputExpense/', inputExpense, name="inputExpense"),
    path('viewExpenses/', viewExpenses, name="viewExpenses"),

]
