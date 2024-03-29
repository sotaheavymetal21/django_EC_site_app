from django.shortcuts import render

# Create your views here.
def index(request):
    val = "Come on!"
    return render(request, "TemplateApp/index.html", context={"value": val})


def home(request, first_name, last_name):
    my_name = f"{ first_name }{ last_name }"
    # my_name = "aa"
    favorite_fruits = ["Apple", "Grape", "Lemon"]
    my_info = {"name": "Sota", "age": 11}
    status = 30
    return render(
        request,
        "home.html",
        context={
            "my_name": my_name,
            "favorite_fruits": favorite_fruits,
            "my_info": my_info,
            "status": status,
        },
    )


def sample1(request):
    return render(request, "sample1.html")


def sample2(request):
    return render(request, "sample2.html")


def sample(request):
    name = "Tatsuya Anegawa"
    height = 185
    weight = 76
    bmi = weight / (height / 100) ** 2
    page_url = "ホームページ: https://www.google.com"
    favorite_fruits = ["Apple", "Grape", "Lemon"]
    msg = """
    my name is
    Tatsuya
    """
    msg2 = "1234567890"
    return render(
        request,
        "sample.html",
        context={
            "name": name,
            "bmi": bmi,
            "page_url": page_url,
            "fruits": favorite_fruits,
            "msg": msg,
            "msg2": msg2,
        },
    )


class Country:
    """インスタンスのプロパティをtemplateに渡して画面上に表示"""

    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital


def sample3(request):
    country = Country("Japan", 100000000, "Tokyo")
    return render(request, "sample3.html", context={"country": country})
