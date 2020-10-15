from django.contrib import admin
from django.urls import path
from Register.views import loginUser, home, logoutUser, inputExpense, registerEmp
from ViewExpenses.views import viewExpenses, trackByEmp, trackByTime, trackByTag, trackByDept

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('loginUser/', loginUser, name="loginUser"),
    path('logoutUser/', logoutUser, name="logoutUser"),
    path('registerEmp/', registerEmp, name="registerEmp"),
    path('inputExpense/', inputExpense, name="inputExpense"),
    path('viewExpenses/', viewExpenses, name="viewExpenses"),
    path('trackByEmp/', trackByEmp, name='trackByEmp'),
    path('trackByTime/', trackByTime, name='trackByTime'),
    path('trackByTag/', trackByTag, name='trackByTag'),
    path('trackByDept/', trackByDept, name='trackByDept'),

]
