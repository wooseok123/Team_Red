from django.shortcuts import render

# Create your views here.
# 메인 페이지
def mainpage(request):
    return render(request, 'index.html')

# 장소 선택 페이지
def choose_place(request):
    return render(request, 'reservation.html')

# 예약 날짜 페이지
def choose_date(request):
    return render(request, '')

# 예약 완료 페이지
def reservation_done(request):
    return render(request, '')