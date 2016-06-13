from django.contrib import admin

# Register your models here.
from .models import Signup
from .forms import SignupForm

class SignupAdmin(admin.ModelAdmin):
	list_display=["full_name","email","date_joined"]
	form = SignupForm

admin.site.register(Signup,SignupAdmin)

