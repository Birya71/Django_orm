from django.http import Http404
from django.shortcuts import render

from .models import Car, Sale


def cars_list_view(request):
    all_cars = Car.objects.all()
    template_name = 'main/list.html'
    context = {
        'cars': all_cars
    }
    return render(request, template_name, context)


def car_details_view(request, car_id):
    result_car = Car.objects.get(id=car_id)
    template_name = 'main/details.html'
    context = {
        'car': result_car
    }
    return render(request, template_name, context)


def sales_by_car(request, car_id):
    try:
        template_name = 'main/sales.html'
        result_car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car_id=car_id)
        context = {
            'car': result_car,
            'sales': sales
        }

        return render(request, template_name, context)
    except Sale.DoesNotExist:
        raise Http404('Car not found')
