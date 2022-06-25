from django.db import models
from datetime import datetime
from login.models import Guest

# Create your models here.
class Reservation(models.Model):
    start_date = models.DateTimeField(default=datetime.now()) # 예약한 날짜
    end_date = models.DateField() # 예약된 날짜
    num_people = models.IntegerField(default=1) # 예약 인원
    payment = models.CharField(default="무통장입금") # 결제 방식

    guest_key = models.ForeignKey(Guest, on_delete=models.CASCADE) # 회원 번호