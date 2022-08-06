
from django.shortcuts import render,redirect
from . models import *
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
			Userdetails = Signup.objects.get(username=request.POST['username'], password=request.POST['password'])
			request.session['username']=Userdetails.username

		except:
			return redirect('onesignup')



def logout(request):
		try:
			del request.session['username']
			return redirect('onesignup')
		except:
			return redirect('onesignup')

	



# Admin login full process

def Adminsignup(request):
	return render(request,'Adminsignup.html')



def adminlogin(request):
	if request.method == 'POST':
		try:
			a = AdminSignup.objects.get(uname = request.POST['uname'] , pwd = request.POST['pwd'])
			request.session['uname'] =  a.uname
		except:
			return redirect('Adminsignup')



def adminlogout(request):
	try:
		del request.session['uname']
		return redirect('Adminsignup')
	except:
		return redirect('Adminsignup')







def Adminpage(request):
	return render(request,'Adminpage.html')


