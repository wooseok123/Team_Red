from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
# 메인 페이지
def mainpage(request):
    # TODO
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('choose_place')
        else: 
            return redirect('index')
            # return render(request, 'bad_login.html')
    else:
        return render(request, 'index.html')

# 장소 선택 페이지
def choose_place(request):
    if request.method == "POST":
        place = request.POST["place"]
        return redirect('choose_date')
    else:
        return render(request, 'reservation.html')

# 예약 날짜 페이지
def choose_date(request):
    if request.method == "POST":
        return redirect('reservation_done')
    else:
        return render(request, '')

# 예약 완료 페이지
def reservation_done(request):
    return render(request, '')