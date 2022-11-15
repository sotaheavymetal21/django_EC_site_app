from django.shortcuts import render

# Create your views here.


class Member:
    def __init__(self, id, name, join_at, picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.picture_path = picture_path


member_list = [
    Member(0, "King_Krull", "2020/04/01", "img/King_krull.jpeg"),
    Member(1, "Enguarde", "2021/04/01", "img/Enguarde.jpeg"),
    Member(2, "Very_Gnawty", "2022/05/01", "img/Very_Gnawty.jpeg"),
    Member(3, "Squawks", "2019/06/01", "img/Squawks.jpeg"),
]
# ホーム画面
def home(request):
    return render(request, "home.html")


# メンバー一覧
def members(request):
    return render(request, "members.html", context={"members": member_list})


# メンバーの画面詳細
def member(request, id):
    return render(request, "member_detail.html", context={"member": member_list[id]})
