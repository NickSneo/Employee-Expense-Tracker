from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Expenses

# Create your views here.


def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['username'] and request.POST['password']:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    return render(request, 'login.html', {'error': 'Email or Password are incorrect'})
            else:
                return render(request, 'login.html', {'error': 'Fields are empty'})
        else:
            return render(request, 'login.html')
    else:
        return redirect("/")


@login_required(login_url="/loginUser")
def home(request):
    if request.method == 'POST':
        if request.POST['action'] == 'registerEmp':
            return render(request, "registerEmp.html")
        elif request.POST['action'] == 'inputExpense':
            return render(request, "inputExpense.html")
        else:
            return render(request, "viewExpenses.html")
    else:
        return render(request, "home.html")


@login_required(login_url="/loginUser")
def registerEmp(request):
    if request.method == 'POST':
        EmpName = request.POST['EmpName']
        EmpId = request.POST['EmpId']
        Dept = request.POST['Dept']
        Salary = request.POST['Salary']
        # print(EmpId, EmpName, Dept, Salary)
        if EmpName and EmpId and Dept and Salary:
            check = Employee.objects.filter(EmpId=EmpId)
            if not check:
                newEmp = Employee(
                    EmpName=EmpName,
                    EmpId=EmpId,
                    Dept=Dept,
                    Salary=Salary
                )
                newEmp.save()
                return redirect("/")
    return render(request, "registerEmp.html")


@login_required(login_url="/loginUser")
def inputExpense(request):
    print("reched")
    if request.method == 'POST':
        print("inside")
        EmpId = request.POST['EmpId']
        Tag = request.POST['Tag']
        Amt = request.POST['Amt']
        # print(EmpId, EmpName, Dept, Salary)
        if EmpId and Tag and Amt:
            newExpense = Expenses(
                EmpId=EmpId,
                Tag=Tag,
                Amt=Amt
            )
            newExpense.save()
            return redirect("/")

    employees = Employee.objects.filter()
    print(employees)
    empIds = []
    for e in employees:
        empIds.append(e.EmpId)
    return render(request, "inputExpense.html", {"empIds": empIds})


@login_required(login_url="/loginUser")
def logoutUser(request):
    logout(request)
    return redirect(home)
