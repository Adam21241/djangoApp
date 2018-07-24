from django.shortcuts import render, get_object_or_404
from .models import Sala, Wydarzenie
import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


dzisiaj = datetime.date.today()
dzisiaj2 = datetime.datetime.today()

def index(request):
    #wyświetla listę wszystkich sal i umożliwia przejście do konkretnej sali
    all_sale = Sala.objects.all()
    return render(request, 'sala/index.html', {'all_sale': all_sale})

def detail(request, sala_id):
    #umożliwia rezerwację sali lub powrót do menu głównego
    sala = get_object_or_404(Sala, pk=sala_id)
    return render(request, 'sala/detail.html', {'sala': sala, 'dzisiaj': dzisiaj})


def rezerwuj(request, sala_id):
    #tu podaje się datę i nick i potwierdza się rezerwację
    sala = get_object_or_404(Sala, pk=sala_id)

    return render(request, 'sala/rezerwuj.html', {'sala': sala})

def rejestracja(request):
    return render(request, 'sala/rejestracja.html')


def confirm(request, sala_id):
    #jeżeli dane są poprawne, to sala zostaje zarezerwowana, w przypadku błędów są wyświetlane odpowiednie ostrzeżenia
    sala = get_object_or_404(Sala, pk=sala_id)

    licznik = 0


    kto = request.POST['field1']
    if kto is '':
        kto = 'Gościu'


    try:
        tempdata = request.POST['field2']
        data = datetime.datetime.strptime(tempdata, '%Y-%m-%d')
        hour1 = request.POST['field3']
        hour2 = request.POST['field4']
        hr1 = int(hour1)
        hr2 = int(hour2)
    except (KeyError, ValueError):
        licznik = -1
        return render(request, 'sala/rezerwuj.html', {'sala': sala, 'kto': kto, 'licznik': licznik})

    if data < dzisiaj2:
        licznik = -2
        return render(request, 'sala/rezerwuj.html', {'sala': sala, 'kto': kto, 'licznik': licznik})

    if hour2 <= hour1:
        licznik = -3
        return render(request, 'sala/rezerwuj.html', {'sala': sala, 'kto': kto, 'licznik': licznik})

    for w in sala.wydarzenie_set.all():
        if (w.podajdate.day == data.day and w.podajdate.month == data.month and w.podajdate.year == data.year and ((hr1 >= w.s_hour and hr1 < w.e_hour) or (hr2 > w.s_hour and hr2 <= w.e_hour))):
            licznik += 1

    if licznik == 0:
        a = Wydarzenie(sala = sala, kto = kto, podajdate = data, s_hour = hr1, e_hour = hr2)
        a.save()

    return render(request, 'sala/rezerwuj.html', {'sala': sala, 'data': data, 'kto': kto, 'licznik': licznik, 'hr1': hr1, 'hr2': hr2})


class UserFormView(View):
    form_class = UserForm
    template_name = 'sala/rejestracja.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            nick = form.cleaned_data['nick']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(nick=nick, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('sala:index')

        return render(request, self.template_name, {'form': form})


