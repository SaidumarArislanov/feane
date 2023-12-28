from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    discount = DiscountModel.objects.all()
    comments = CommentModel.objects.all()
    all = MenuModel.objects.all()
    context = {
        'discounts': discount,
        'comments': comments,
        'all': all
    }
    return render(request, template_name='index.html', context=context)
