from django.shortcuts import render
from Task.models import Addproduct, Addmove
from Task.forms import ProductForm, MoveForm

# Create your views here.

def home(request):
    return render(request, 'Task/home.html')

def product(request):
    products = Addproduct.objects.all() 
    return render(request, "Task/Product.html",{"object": products})

def insert(request):
    if request.method == "POST":
        inser = ProductForm(request.POST or None)
        if inser.is_valid():
            inser.save()
    return render(request, "Task/Add.html")

def goods(request):
    moves = Addmove.objects.all()
    return render(request, "Task/Goods.html",{"objects": moves})

def move(request):
    if request.method == "POST":
        appe = MoveForm(request.POST or None)
        if appe.is_valid():
            appe.save()

    return render(request, "Task/Move.html")

