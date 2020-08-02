from django.forms import ModelForm
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):
	class Meta:
		model = Post
		exclude = ['date_posted', 'author']


class SimpleForm(forms.Form):
	message = forms.CharField(label='', max_length=200, required=True,
		widget=forms.Textarea(attrs={'rows': 3, 'cols': 68, 'placeholder': 'Enter your note here...'}))