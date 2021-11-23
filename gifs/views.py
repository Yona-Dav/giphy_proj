from django.shortcuts import render
from .models import Gif, Category
# Create your views here.

def homepage(request):
    gifs = Gif.objects.all()
    return render(request, 'homepage.html', {'all_gifs': gifs})

def category(request, category_id):
    cat = Category.objects.get(id=category_id)
    gifs = cat.gifs.all()
    return render(request, 'category.html', {'gifs': gifs, 'category':cat})

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'all_categories': categories})

def single_gif(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    return render(request, 'gif.html', {'gif': gif})