from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('todolist/', views.todolist, name='todolist'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
