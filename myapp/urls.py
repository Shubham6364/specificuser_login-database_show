
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('myapp.urls'))
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
