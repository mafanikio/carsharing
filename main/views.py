from django.shortcuts import render, redirect
from .models import Employee, Car, Order, Services, Detail


def home(response):
    return render(response, 'main/main.html', {})


def workers(response):
    people = Employee.objects.all()
    people = [elem for elem in people] * 5
    return render(response, 'main/workers.html', {'workers': people})


def service(response):
    things = Services.objects.all()
    things = [elem for elem in things] * 5
    return render(response, 'main/service.html', {'things': things})


def orders(response):
    orders = Order.objects.all()
    orders = [elem for elem in orders] * 5
    return render(response, 'main/orders.html', {'orders': orders})


def cars(response):
    autos = Car.objects.all()
    autos = [elem for elem in autos] * 5
    return render(response, 'main/cars.html', {'cars': autos})


def view(response):
    return render(response, 'main/view.html', {})



def search(response):
    if response.method == 'POST':
        year = response.POST.get('caryear', 0)
        type = response.POST.get('selector', 0)
        maker = response.POST.get('carmaker', 0)
        model = response.POST.get('carmodel', 0)
        if int(type) == 1:
            tp = 'Легковые'
        elif int(type) == 2:
            tp = 'Автобусы'
        elif int(type) == 3:
            tp = 'Грузовые'
        else:
            tp = 0
        sort = Car.objects.get(maker=maker, type=tp)
        return render(response, 'main/cars.html', {'cars': [sort]})
    else:
        return render(response, 'main/search.html', {})
