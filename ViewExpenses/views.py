from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Register.models import Employee, Expenses
import datetime
import pytz
# Create your views here.


@login_required(login_url="/loginUser")
def viewExpenses(request):
    return render(request, "viewExpenses.html")


@login_required(login_url="/loginUser")
def trackByEmp(request):
    expenses = []
    tagExpense = {}
    total = 0
    name = ""
    salary = ""
    if request.method == 'POST':
        EmpId = request.POST['EmpId']
        emp_expenses = Expenses.objects.filter(EmpId=EmpId)

        employee = Employee.objects.get(EmpId=EmpId)
        name = employee.EmpName
        salary = employee.Salary
        startdate = pytz.utc.localize(
            datetime.datetime.now() - datetime.timedelta(days=30))
        for e in emp_expenses:
            if e.Time >= startdate:
                expenses.append(
                    {'time': e.Time, 'tag': e.Tags, 'amount': e.Amount})
                total += e.Amount
                tagExpense[e.Tags] = tagExpense.get(e.Tags, 0) + e.Amount
    employees = Employee.objects.all()
    empIds = []
    for e in employees:
        empIds.append(e.EmpId)
    return render(request, 'trackByEmp.html', {"empIds": empIds, "expenses": expenses, "total": total, "name": name, "salary": salary, "tagExpense": tagExpense})


@login_required(login_url="/loginUser")
def trackByTime(request):
    # Code to handle post request
    today = pytz.utc.localize(
        datetime.datetime.now() - datetime.timedelta(days=1))
    week = pytz.utc.localize(
        datetime.datetime.now() - datetime.timedelta(days=7))
    month = pytz.utc.localize(
        datetime.datetime.now() - datetime.timedelta(days=30))

    print(today)
    print(week)
    print(month)
    todayExpense = 0
    weekExpense = 0
    monthExpense = 0
    all_expenses = Expenses.objects.all()
    for exp in all_expenses:
        if exp.Time >= today:
            todayExpense += exp.Amount
        if exp.Time >= week:
            weekExpense += exp.Amount
        if exp.Time >= month:
            monthExpense += exp.Amount

    return render(request, 'trackByTime.html', {"todayExpense": todayExpense, "weekExpense": weekExpense, "monthExpense": monthExpense})


@login_required(login_url="/loginUser")
def trackByTag(request):
    tag_list = ['Personal', 'Insurance',
                'Travel', 'Rent', 'Relocation', 'Misc']

    tag_expenses = Expenses.objects.all()
    tagExpense = {}
    startdate = pytz.utc.localize(
        datetime.datetime.now() - datetime.timedelta(days=30))
    for t in tag_expenses:
        if t.Time >= startdate:
            tagExpense[t.Tags] = tagExpense.get(t.Tags, 0) + t.Amount
    if request.method == 'POST':
        expenses = []
        tag = request.POST['Tag']
        for t in tag_expenses:
            if t.Time >= startdate:
                if t.Tags == tag:
                    expenses.append(
                        {'time': t.Time, 'id': t.EmpId.EmpId, 'amount': t.Amount, 'name': t.EmpId.EmpName})
                tagExpense[t.Tags] = tagExpense.get(t.Tags, 0) + t.Amount
        if tag in tagExpense:
            total = tagExpense[tag]
        else:
            total = 0

        return render(request, 'trackByTag.html', {"tags": tag_list, "expenses": expenses, "sum": total, "name": tag, "tagExpense": tagExpense})
    else:
        return render(request, 'trackByTag.html', {"tags": tag_list, "tagExpense": tagExpense})


@login_required(login_url="/loginUser")
def trackByDept(request):
    dept_list = ['HR', 'Tech', 'Finance',
                 'Marketing', 'Production', 'Stratergy']
    all_expenses = Expenses.objects.all()
    deptExpense = {}
    startdate = pytz.utc.localize(
        datetime.datetime.now() - datetime.timedelta(days=30))
    for i in all_expenses:
        if i.Time >= startdate:
            empInfo = Employee.objects.get(EmpId=i.EmpId.EmpId)
            deptExpense[empInfo.Dept] = deptExpense.get(
                empInfo.Dept, 0) + i.Amount
    return render(request, 'trackByDept.html', {'deptExpense': deptExpense})
