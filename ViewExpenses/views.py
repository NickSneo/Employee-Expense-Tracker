from django.shortcuts import render

# Create your views here.


def viewExpenses(request):
    return render(request, "viewExpenses.html")
