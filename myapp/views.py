
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















def login(request):
	if request.method == 'POST':
		try:
			Userdetails = Signup.objects.get(username=request.POST['username'], password=request.POST['password'])
			request.session['username']=Userdetails.username

		except:
			return redirect('onesignup')

	return render(request,'onelogin.html')



def logout(request):
		try:
			del request.session['username']
			return redirect('login')
		except:
			return redirect('login')

	







def adminlogin(request):
	if request.method == 'POST':
		try:
			a = Adminsignup.objects.get(uname = request.POST['uname'] , pwd = request.POST['pwd'])
			request.session['uname'] =  a.uname
		except:
			return redirect('Adminsignup')

	return render(request,'Adminsignup.html')



def adminlogout(request):
	try:
		del request.session['uname']
		return redirect('adminlogin')
	except:
		return redirect('adminlogin')







def Adminpage(request):
	return render(request,'Adminpage.html')


