from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='all_gifs'),
    path('category/<int:category_id>/', views.category, name='single_category'),
    path('category/all/', views.all_categories, name='all_categories'),
    path('homepage/<int:gif_id>/', views.single_gif, name='single_gif'),
    path('homepage/<int:gif_id>/<int:liked>/', views.gif_like_action, name='like_link')
]