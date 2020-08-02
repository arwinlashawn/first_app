from django.shortcuts import render
from django.contrib import messages
from django.db import models
from django.views.generic import ListView, CreateView
from .models import Post
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, SimpleForm

# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all().order_by('-date_posted')
	}
	return render(request, 'notes/home.html', context)


# def register(request):
# 	if request.method == 'POST':
# 		form = UserRegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'Your account has been created. Log in now to start posting notes!')
# 			return redirect('login')
# 	else:
# 		form = UserRegisterForm()
# 	return render(request, 'users/register.html', {'form': form})

def create_post(request):
	if request.method == 'POST':
		form = SimpleForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else:
		form = SimpleForm()

	return render(request, 'notes/home.html', {'form': form})


class PostListView(ListView):
	model = Post
	template_name = 'notes/home.html' 
	context_object_name = 'posts'
	# notice that latest message is at the bottom, gotta change it
	ordering = ['-date_posted']

def create(request): # finally!

	if request.method == 'POST':
		form = SimpleForm(request.POST)

		if form.is_valid():
			a = request.user
			n = form.cleaned_data["message"]
			t = Post(content=n, author=a)
			t.save()
			#context = { 'posts': t.objects.all()}

		return HttpResponseRedirect("/")

	else:
		form = SimpleForm()

	context = {
		'form': form,
		'posts': Post.objects.all().order_by('-date_posted')
	}	

	return render(request, "notes/home.html", context)






def about(request):
	return render(request, 'notes/about.html', {'title': 'About'})

# looking for notes/post_list.html
# app/model_viewtype.html