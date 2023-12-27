from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, template_name='index.html')