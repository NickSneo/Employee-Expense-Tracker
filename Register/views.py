from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
        if request.POST['register']:
            return render(request, "register.html")
        else:
            return render(request, "viewsExpenses.html")
        hi = "hi"
        return render(request, "home.html", {hi: hi})
    else:
        return render(request, "home.html")


# def register()

@login_required(login_url="/loginUser")
def logoutUser(request):
    logout(request)
    return redirect(home)
