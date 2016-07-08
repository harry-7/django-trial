from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm,CommandForm
from django.contrib.auth import authenticate, login, logout

import os
# Create your views here.

def home(request):
    context = {

    }
    lis = request.session.keys()
    for key in list(lis):
        context[key] = request.session[key]
        if key in ["success_message","failure_message"]:
            request.session.pop(key)
    return render(request, "home.html", context)


def signup(request):
    title = 'Welcome '
    if request.user.is_authenticated():
        title += str(request.user)
    else:
        title += "Guest"

    form = SignupForm(request.POST or None)

    context = {
        "title": "Signup",
        "form": form,
        "formname": "Register",
    }
    if form.is_valid():
        instance = form.save()
        success_message = "SignUp Success"
        context["success_message"] = success_message

    return render(request, "form.html", context)


def form_login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
        "formname": "Login",
        "title":"Login",
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                success_message = "Logged In Successfully"
                request.session["success_message"] = success_message
                return redirect("/")
        else:
            context["failure_message"] = "Username/Password combination doesnt exist"
    return render(request, "form.html", context)


def form_logout(request):
    logout(request)
    success_message = "Logged out Successfully"
    request.session["success_message"] = success_message
    return redirect("/")

@login_required
def command(request):
    form = CommandForm(request.POST or None)
    if request.user.username != "harry7":
        request.session["failure_message"] = "Access Restricted (Only for harry7)"
        return redirect("/")
    context={
        "form":form,
        "data":"Welcome "+request.user.username,
        "title": "Command Interface",
        "formname": "Execute",
    }
    print "Validity",form.is_valid()
    if form.is_valid():
        cmd = form.cleaned_data.get("command")
        data = os.popen(cmd).readlines()
        data = "".join(data)
        context["data"]=data
        print "data",data
    return render(request,"form.html",context)