from django.shortcuts import render, redirect
from .models import Gif, Category

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html', {'all_gifs': Gif.objects.all()})

def category(request, category_id):
    cat = Category.objects.get(id=category_id)
    gifs = cat.gifs.all()
    return render(request, 'category.html', {'gifs': gifs, 'category':cat})

def all_categories(request):
    return render(request, 'categories.html', {'all_categories': Category.objects.all()})

def single_gif(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    return render(request, 'gif.html', {'gif': gif})

def gif_like_action(request, gif_id, liked):
    gif = Gif.objects.get(id=gif_id)
    if liked:
        gif.likes += 1
    else:
        gif.likes -= 1
    gif.save()
    return redirect('single_gif', gif.id)