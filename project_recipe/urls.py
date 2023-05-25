from django.contrib import admin
from django.urls import path
from recipe import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),
    path('category_list/', views.category_list),
    path('', views.main, name='main')
]