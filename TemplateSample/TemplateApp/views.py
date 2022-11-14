from django.shortcuts import render

# Create your views here.
def index(request):
    val = "Come on!"
    return render(request, "index.html", context={"value": val})


def home(request):
    my_name = "Sota Anegawa"
    favorite_fruits = ["Apple", "Grape", "Lemon"]
    my_info = {
        "name": "Sota",
        "age": 24
    }
    return render(request, "home.html", context={
        "my_name": my_name,
        "favorite_fruits": favorite_fruits,
        "my_info": my_info
    })
