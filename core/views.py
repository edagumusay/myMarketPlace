from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category, Item
from .forms import SignupForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    return render(request, 'core/index.html', {
        'items': items,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form' : form
    })

def logout_user(request):
    logout(request)
    return redirect('/')


def index(request):
    items = Item.objects.filter(is_sold=False)
    paginator = Paginator(items, 3)

    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1) 
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'core/index.html', {'items': items})