from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
	a = Specific.objects.all() 


	if request.method=='POST':
		fname = request.POST.get('fname')
		sname = request.POST.get('sname')


		a = Specific(fname=fname , sname=sname)

		if request.method == 'POST':
			try:
				Userdetails = Signup.objects.get (username=request.POST['username'], password=request.POST['password'])
				request.session['username']=Userdetails.username
				return redirect('index')

			except:
				pass


		user_login = Signup.objects.get(username=request.session['username'])
		a.username = user_login
		a.save()
		


		return redirect('index')

	

	return render(request,'index.html',{'a':a})












def onesignup(request):
	return render(request,'onelogin.html')



def login(request):
	if request.method == 'POST':
		try:
			Userdetails = Signup.objects.get (username=request.POST['username'], password=request.POST['password'])
			request.session['username']=Userdetails.username
			return redirect('index')

		except:
			pass



def logout(request):
	try:
		del request.session['username']
		return redirect('onesignup')
	except:
		return render(request,'onelogin.html')


