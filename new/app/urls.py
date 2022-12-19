from django.urls import path

from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('SignUp', SingUp.as_view(), name='SignUp'),
    path('Login', Log.as_view(), name='Login'),
    path('Logout', Logout, name='Logout'),
    path('Make_order', form, name='Form'),
    path('Halls', Halls, name='Halls'),
    path('Dishes', Dishes_show, name='Dishes'),
    path('edit/<int:id>/', Edit, name='edit'),
    path('delete/<int:id>/', Delete, name='delete')
]