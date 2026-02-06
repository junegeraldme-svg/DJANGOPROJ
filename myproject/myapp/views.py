from django.shortcuts import render
import requests

def homepage(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    return render(request, "myapp/homepage.html", {"posts": posts})

def todolist(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    tasks = response.json()
    return render(request, "myapp/todolist.html", {"tasks": tasks})

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")
