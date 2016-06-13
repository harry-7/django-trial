from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = ['email','full_name']

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		if " " not in full_name:
			raise forms.ValidationError("Enter Full Name with last name")
		return full_name