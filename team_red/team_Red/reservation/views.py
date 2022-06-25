from django.shortcuts import redirect, render

# Create your views here.
# 메인 페이지
def mainpage(request):
    # TODO
    if request.method == "POST":
        return redirect('choose_place')
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