from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Register.models import Employee, Expenses
# Create your views here.

@login_required(login_url="/loginUser")
def viewExpenses(request):
    return render(request, "viewExpenses.html")

@login_required(login_url="/loginUser")
def trackByEmp(request):
	expenses = []
	sum = 0
	name = ""
	salary=""
	if request.method == 'POST':
		EmpId = request.POST['EmpId']
		emp_expenses = Expenses.objects.filter(EmpId=EmpId)

		name = Employee.objects.filter(EmpId=EmpId)[0].EmpName
		salary = Employee.objects.filter(EmpId=EmpId)[0].Salary
		
		for e in emp_expenses:
			expenses.append({'time':e.Time, 'tag':e.Tags, 'amount':e.Amount})
			sum+=e.Amount
	employees = Employee.objects.filter()
	empIds = []
	for e in employees:
		empIds.append(e.EmpId)
	return render (request, 'trackByEmp.html',{"empIds": empIds, "expenses":expenses,"sum":sum,"name":name,"salary":salary})

@login_required(login_url="/loginUser")
def trackByTime(request):
	# Code to handle post request
	return render (request, 'trackByTime.html')

@login_required(login_url="/loginUser")
def trackByTag(request):
	expenses = []
	sum = 0
	tag = ""
	if request.method == 'POST':
		tag = request.POST['Tag']
		tag_expenses = Expenses.objects.filter(Tags=tag)
		
		for t in tag_expenses:
			print(t)
			expenses.append({'time':t.Time, 'id': t.EmpId, 'amount':t.Amount})
			sum+=t.Amount

	tag_list = []
	for item in Expenses.objects.filter():
		if str(item.Tags) not in tag_list:
			tag_list.append(str(item.Tags))
	return render (request, 'trackByTag.html',{"tags": tag_list, "expenses":expenses,"sum":sum,"name":tag})