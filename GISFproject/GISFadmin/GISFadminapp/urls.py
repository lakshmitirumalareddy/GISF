from django.urls import path

from .views import NewUserCreate, userregister, loginView, logout_view, homepage, about, mainmenu
app_name = 'GISFadmin'

urlpatterns = [
  path('NewUser/', NewUserCreate, name='NewUser'),
  path('NewUserReg/', userregister, name='NewUserReg'),
  path('Login/', loginView, name='Login'),
  path('Logout/', logout_view, name='Logout'),
  path('Home/', homepage, name='Home'),
  path('About/', about, name='About'),
  path('MainMenu/', mainmenu, name='MainMenu')

]