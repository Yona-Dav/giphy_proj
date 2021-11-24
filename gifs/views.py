from django.shortcuts import render, redirect , get_object_or_404 , get_list_or_404
from .models import Gif, Category
from .forms import GifForm

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html', {'all_gifs': Gif.objects.all()})

def category(request, category_id):
    cat = Category.objects.get(id=category_id)
    gifs = cat.gifs.all()
    return render(request, 'category.html', {'gifs': gifs, 'category':cat})

def all_categories(request):
    return render(request, 'categories.html', {'all_categories': Category.objects.all()})

def gif_view(request, gif_id):
    gif = get_object_or_404(Gif, id=gif_id)
    return render(request, 'gif.html', {'gif': gif})

def gif_like_action(request, gif_id, liked):
    gif = Gif.objects.get(id=gif_id)
    if liked:
        gif.likes += 1
    else:
        gif.likes -= 1
    gif.save()
    return redirect('single_gif', gif.id)

def test_page(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            gif = Gif.objects.create(**form.cleaned_data)
            return redirect('single_gif', gif.id)
    if request.method == 'GET':
        form = GifForm()
    return render(request, 'add_gif.html',{'form':form})

def gifs_by_likes(request):
    gifs = get_list_or_404(Gif, likes__gt=0)
    print(gifs)
    gifs.sort(key=lambda x:x.likes, reverse=True)
    return render(request, 'homepage.html', {'all_gifs': gifs})