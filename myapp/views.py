from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):

	a = Specific.objects.filter(username = request.session['username'])


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



def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		repeatpassword = request.POST.get('repeatpassword')
		
		
		


		s = Signup(username = username , email=email , password=password , repeatpassword=repeatpassword)
		s.save()
		return redirect('login')

	return render(request,'signup.html')


def login(request):
	if request.method == 'POST':
		try:
			Userdetails = Signup.objects.get (username=request.POST['username'], password=request.POST['password'])
			request.session['username']=Userdetails.username
			return redirect('index')

		except:
			pass

	return render(request,'login.html')



def logout(request):
	try:
		del request.session['username']
		return redirect('login')
	except:
		pass
	return render(request,'login.html')