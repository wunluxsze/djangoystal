from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import Order_form
from .models import Dishes, Hall, Order
from django.contrib.auth import login


def Edit(request, id):
    if request.method == 'POST':
        form = Order_form(request.POST)

        if form.is_valid():

            dishes_id = form.cleaned_data['dishes']
            dishes_ids = Dishes.objects.filter(id__in=dishes_id)

            order_obj = Order.objects.get(id=id)

            order_obj.customer_name = form.cleaned_data['customer_name']
            order_obj.hall_id = form.cleaned_data['hall']
            order_obj.date = form.cleaned_data['date']
            order_obj.people_count = form.cleaned_data['people_count']
            order_obj.times_day = Order_form.Times_Data_Choice[int(form.cleaned_data['times_day']) - 1][-1]



            order_obj.dishes.set(dishes_ids, through_defaults={})
            order_obj.save()
            return redirect('home')

        else:
            print('is_not_valid')
    else:
        form = Order_form()

    return render(request, 'app/form.html', {'form': form})


def Delete(request, id):
    try:
        order = Order.objects.get(id=id)
    except:
        return HttpResponseNotFound('<h2>Person not found</h2>')
    order.delete()
    return redirect('home')


def index(request):
    create_Dishes()
    create_Hall()
    user = request.user
    if user.is_staff:
        order = Order.objects.all()
    else:
        order = Order.objects.filter(id_user=user.id)
    return render(request, 'app/index.html', {'Orders': order})


def Dishes_show(request):
    return render(request, 'app/Dishes.html', {'Dishes': Dishes.objects.all()})


def Halls(request):
    return render(request, 'app/Halls.html', {'Halls': Hall.objects.all()})


def form(request):
    if request.method == 'POST':
        form = Order_form(request.POST)

        if form.is_valid():

            dishes_id = form.cleaned_data['dishes']
            dishes_ids = Dishes.objects.filter(id__in=dishes_id)


            order_obj = Order.objects.create(
                customer_name=form.cleaned_data['customer_name'],
                hall_id=form.cleaned_data['hall'],
                date=form.cleaned_data['date'],
                times_day=Order_form.Times_Data_Choice[int(form.cleaned_data['times_day'])-1][-1],
                people_count=form.cleaned_data['people_count'],
                id_user=request.user.id
            )

            order_obj.dishes.set(dishes_ids, through_defaults={})

            return redirect('home')

        else:
            print('is_not_valid')
    else:
        form = Order_form()

    return render(request, 'app/form.html', {'form': form})


class SingUp(CreateView):
    form_class = UserCreationForm
    template_name = 'app/SignUp.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form, 'title': 'Reg'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Log(LoginView):
    form_class = AuthenticationForm
    template_name = 'app/Login.html/'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form, 'title': 'Log'}


def Logout(request):
    logout(request)
    return redirect('home')


def create_Dishes():
    if Dishes.objects.all().count() == 0:
        Dishes.objects.create(name='суп', compound='из овощей')
        Dishes.objects.create(name='пиво', compound='из молока')
        Dishes.objects.create(name='мясо', compound='не мясо')
        Dishes.objects.create(name='сыр', compound='для меня')
        Dishes.objects.create(name='пицца', compound='с ананасами')


def create_Hall():
    if Hall.objects.all().count() == 0:
        Hall.objects.create(name='1 зал, нормальный', info='для бедных')
        Hall.objects.create(name='2 зал, средненький', info='больше 60 людей')
        Hall.objects.create(name='3 зал, денег на такой не хватит', info='огромный')
