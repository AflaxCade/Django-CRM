from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.

def home(request):

    # display all the records
    records = Record.objects.all().values()

    # check to see if the user is logged in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate the user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # messages.success(request, f'Welcome {username}!')
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
        
    else:
        return render(request, 'home.html', {'records':records})


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('home')
