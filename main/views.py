from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, Car, Order, Services, Detail
from .forms import CreateNewList



def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == 'POST':
            print(response.POST)
            if response.POST.get('save'):
                for item in ls.item_set.all():
                    if response.POST.get(f'c{item.id}') == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get('newItem'):
                txt = response.POST.get('new')
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print('Invalid')
        return render(response, 'main/list.html', {"ls": ls})
    return render(response, 'main/view.html', {})


def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            t = ToDoList(name=name)
            t.save()
            response.user.todolist.add(t)
            return HttpResponseRedirect(f'/{t.id}')
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})


def home(response):
    return render(response, 'main/main.html', {})


def workers(response):
    people = Employee.objects.all()
    people = [elem for elem in people] * 5
    return render(response, 'main/workers.html', {'workers': people})


def service(response):
    things = Detail.objects.all()
    things = [elem for elem in things] * 5
    return render(response, 'main/service.html', {'workers': things})


def orders(response):
    return render(response, 'main/orders.html', {})


def cars(response):
    autos = Car.objects.all()
    autos = [elem for elem in autos] * 5
    return render(response, 'main/cars.html', {'cars':autos})


def view(response):
    return render(response, 'main/view.html', {})
