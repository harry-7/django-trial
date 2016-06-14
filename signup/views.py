from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    context={

    }
    for key,value in request.session.iteritems():
        context[key]=value
    return render(request, "home.html", context)

def signup(request):
    title = 'Welcome '
    if request.user.is_authenticated():
        title += str(request.user)
    else:
        title += "Guest"

    form = SignupForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
        "formname":"Register",
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
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                success_message = "Logged In Successfully"
                request.session["success_message"] = success_message
                return redirect("/")
        else:
            context["failure_message"]="Username/Password combination doesnt exist"
    return render(request, "form.html", context)

def form_logout(request):
    logout(request)
    success_message = "Logged out Successfully"
    request.session["success_message"] = success_message
    return redirect("/")
