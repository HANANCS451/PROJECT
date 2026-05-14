from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal
from .forms import MealForm
from django.db.models import Q

def home(request):
    return render(request, 'menu/index.html')

def meals_list(request):
    query = request.GET.get('q')
    meals = Meal.objects.all()
    if query:
        meals = meals.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)    )
    return render(request,'menu/list.html',{'meals': meals})

def meal_detail(request, id):
    meal = get_object_or_404(Meal, id=id)
    return render( request, 'menu/detail.html', {'meal': meal}   )

def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meals_list')
    else:
        form = MealForm()
    return render(request,'menu/add.html',{'form': form}  )
