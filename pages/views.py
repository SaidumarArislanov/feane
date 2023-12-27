from django.shortcuts import render, redirect
from pages.models import MenuModel, ResevationModel, PersonModel
from pages.forms import ReservationForm


# Create your views here.

def menu_products(request):
    products = MenuModel.objects.all()
    return render(request, 'index.html', {'products': products})


def home(request):
    num_of_people = ResevationModel.objects.all()
    context = {
        'persons': num_of_people,
    }
    return render(request, template_name='index.html', context=context)


def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
    else:
        form = ReservationForm()

    return render(request, 'index.html', )