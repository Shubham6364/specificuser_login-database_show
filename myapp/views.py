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











# Staff login full process
def onesignup(request):
	return render(request,'onelogin.html')



def login(request):
	if request.method == 'POST':
		try:
			Userdetails = Signup.objects.get (username=request.POST['username'], password=request.POST['password'])
			print('Userdetails')
			request.session['username']=Userdetails.username

		except:
			return redirect('onesignup')



def logout(request):
	try:
		del request.session['username']
		return redirect('onesignup')
	except:
		return redirect('onelogin')

	return render(request,'onelogin.html')



# Admin login full process

def Adminsignup(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')

		b = Admin_Signup(uname = uname , pwd = pwd).save()
	return render(request,'onelogin.html')



def adminlogin(request):
	if request.method == 'POST':
		try:
			Userdetails = Admin_Signup.objects.get (uname=request.POST['uname'], pwd=request.POST['pwd'])
			print('Userdetails')
			request.session['uname']=Userdetails.uname

		except:
			pass


def Adminpage(request):
	return render(request,'Adminpage.html')