from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	### IMPORTANT ###
	# to ensure that already used email addresses can't be used when signing up!
	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError("The email you entered has already been used.")
		return self.cleaned_data['email']

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']