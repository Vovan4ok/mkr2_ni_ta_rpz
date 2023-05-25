from django.shortcuts import render
from .models import Recipe, Category
from django.db.models import Count


def main(request):
    recipes = Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'main.html', {'recipes': recipes})


def category_list(request):
    categories = Category.objects.all()
    category_counts = []
    for category in categories:
        category_counts.append({
            'name': category.name,
            'count': category.categories.count()
        })
    return render(request, 'category_list.html', {'category_counts': category_counts})