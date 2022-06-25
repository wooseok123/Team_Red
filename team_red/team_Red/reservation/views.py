from django.shortcuts import get_object_or_404, redirect, render
from .models import Reservation
from .forms import ReservationForm
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
    '''if request.method == 'POST' or request.method == 'FILES':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('choose_date', form.auto_id)
    else:'''
    return render(request, 'reservation.html')

# 예약 날짜 페이지
def choose_date(request, pk):
    if request.method == "POST": 
        return redirect('choose_num')
    else:
        return render(request, 'when.html')

def choose_num(request):
    if request.method == "POST":
        return redirect('reservation_done')
    else:
        return render(request, 'how.html')

# 예약 완료 페이지
def reservation_done(request):
    return render(request, 'success.html')