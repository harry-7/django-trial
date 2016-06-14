from django.shortcuts import render
from .forms import SignupForm


# Create your views here.

def home(request):

    return render(request, "home.html", {})

def signup(request):
    title = 'Welcome '
    if request.user.is_authenticated():
        title += str(request.user)
    else:
        title += "Guest"

    form = SignupForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        instance = form.save()
        success_message = "SignUp Success"
        context["success_message"] = success_message

    return render(request, "form.html", context)
