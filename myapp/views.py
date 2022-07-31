from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
	a = specific.objects.filter(user=request.user)
	if request.method=='POST':
		fname = request.POST.get('fname')
		sname = request.POST.get('sname')

		a = specific(fname=fname , sname=sname)
		a.save()

		return redirect('index')

	
		

	return render(request,'index.html',{'a':a})



def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword = request.POST['repeatpassword']
		
		
		
		


		# create the user
		user = User.objects.create_user(username, email , password)
		user.repeatpassword = repeatpassword
		user.save()
		return redirect('login')

	return render(request,'signup.html')


def login(request):
	if request.method == 'POST':
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']

		user = auth.authenticate(request,username=loginusername, password=loginpassword)
		if user is not None:
			auth.login(request,user)
			return redirect('index')

	return render(request,'login.html')



def logout(request):
		auth.logout(request)
		return redirect('login')