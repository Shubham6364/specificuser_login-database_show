
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('myapp.urls'))
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('onesignup',views.onesignup,name='onesignup'),
    # path('Adminsignup',views.Adminsignup,name='Adminsignup'),
    path('Adminpage',views.Adminpage,name='Adminpage'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    # path('Adminsignup',views.Adminsignup,name='Adminsignup'),
    path('adminlogin',views.adminlogin,name='adminlogin'),

   
]