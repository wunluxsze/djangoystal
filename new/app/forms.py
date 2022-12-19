from django import forms
from .models import Dishes, Hall


class Order_form(forms.Form):
    customer_name = forms.CharField(max_length=50, label='ФИО: ')

    COICE_HALL = [(i.id, i.name) for i in Hall.objects.all()]
    hall = forms.ChoiceField(choices=COICE_HALL, label='Зал: ')

    COICE_DISHES = [(i.id, i.name) for i in Dishes.objects.all()]
    dishes = forms.MultipleChoiceField(choices=COICE_DISHES, label='Блюда: ')

    date = forms.DateField(label='Дата: ', widget=forms.DateInput(attrs={'type': 'date'}))

    Times_Data_Choice = [ (1, 'Утро'), (2, 'День'), (3, 'Вечер' ) ]

    times_day = forms.ChoiceField(choices=Times_Data_Choice, label='Время дня: ')

    checkbox = CheckBox = forms.CharField(label='Согласие на обработку персональных данных', widget=forms.CheckboxInput())

    people_count = forms.IntegerField(label='Кол-во человек:')

